# SPDX-FileCopyrightText: 2023 pukkamustard <pukkamustard@posteo.net>
#
# SPDX-License-Identifier: AGPL-3.0-or-later

""" Class providing decoder to read ERIS encoded content. """

from io import UnsupportedOperation
from dataclasses import dataclass
from eris.read_capability import ReadCapability
from eris.crypto import *
from eris import base32


class DecodeError(Exception):
    """General ERIS decode error"""

    def __init__(self, message):
        super().__init__(message)


class InvalidBlockHash(LookupError, DecodeError):
    """Exception that is raised when de-referenced block has invalid hash"""

    def __init__(self, ref, block):
        self.ref = ref
        self.block = block
        block_hash = Blake2b_256(block)
        self.message = f"Expecting block with reference {base32.encode(ref)} but got {base32.encode(block_hash)}"
        super().__init__(self.message)


class InvalidPadding(DecodeError):
    """Exception that is raised when invalid padding is encountered"""

    def __init__(self):
        pass


class MissingBlock(DecodeError):
    """Exception that is raised when a block is missing"""

    def __init__(self, ref):
        self.ref = ref
        self.message = f"Block {base32.encode(ref)} could not be dereferenced"
        super().__init__(self.message)


class InvalidBlockSize(DecodeError):
    """Exception that is raised when a block has invalid size"""

    def __init__(self, block, expected_block_size):
        self.block = block
        self.message = f"Expecting block of size {expected_block_size}, but block has size {len(block)}"
        super().__init__(self.message)


@dataclass
class ReferenceKeyPair:
    """A reference-key pair"""

    ref: str
    key: str

    def __repr__(self):
        return "<ReferenceKeyPair>"


def _level_rk_width(block_size, level):
    """Returns the width of content that can be reached by one
    reference-key pair at this level."""
    arity = block_size / 64
    return int(arity ** (level - 1)) * block_size


@dataclass
class InternalNode:
    """An inernal node along with an integer that notes the current
    position and whether the node is the final node in a level of the
    tree."""

    reference_key_pairs: list[ReferenceKeyPair]
    level: int
    cur: int
    level_count: int  # ofset of the initial ref-key pair
    final: bool

    def current_reference_key_pair(self):
        return self.reference_key_pairs[self.cur]

    def level_range(self, block_size):
        start = _level_rk_width(block_size, self.level) * self.level_count
        end = _level_rk_width(block_size, self.level) * (
            self.level_count + len(self.reference_key_pairs)
        )
        return (start, end)

    def range(self, block_size):
        start = _level_rk_width(block_size, self.level) * (self.level_count + self.cur)
        end = start + _level_rk_width(block_size, self.level)
        return (start, end)


@dataclass
class LeafNode:
    """Represents a leaf node."""

    content: bytes
    offset: int
    level_count: int
    final: bool
    level = 0

    def range(self, block_size):
        start = self.level_count * block_size
        end = start + min(block_size, len(self.content))
        return (start, end)

    def remaining_bytes(self):
        return len(self.content) - self.offset

    def read(self, size):
        n = min(size, self.remaining_bytes())
        out = self.content[self.offset : self.offset + n]
        self.offset = self.offset + n
        return out


class Decoder:
    """Read ERIS encoded content."""

    def __init__(self, store, read_capability):

        if isinstance(read_capability, ReadCapability):
            self.read_capability = read_capability
        else:
            self.read_capability = ReadCapability(read_capability)

        self.store = store
        self.path = [
            InternalNode(
                [
                    ReferenceKeyPair(
                        self.read_capability.root_ref, self.read_capability.root_key
                    )
                ],
                self.read_capability.level + 1,
                0,  # cur
                0,  # level_count
                True,  # final
            )
        ]

    def _unpad(self, content):
        i = self.read_capability.block_size - 1
        while i > 1:
            if content[i] == 0x00:
                i = i - 1
            elif content[i] == 0x80:
                break
            else:
                raise InvalidPadding()
        if i > 1:
            return content[0:i]
        else:
            return bytes(0)

    async def _get_node(self, ref, key, level, level_count, final):
        block = await self.store.get(ref, block_size=self.read_capability.block_size)

        if not block:
            raise MissingBlock(ref)

        if not len(block) == self.read_capability.block_size:
            raise InvalidBlockSize(block, self.read_capability.block_size)

        if not ref == Blake2b_256(block):
            raise InvalidBlockHash(ref, block)

        # nonce for level
        nonce = bytearray(12)
        nonce[0] = level

        # de-crypt block
        node = ChaCha20(block, key, nonce)

        if level == 0:
            if final:
                return LeafNode(self._unpad(node), 0, level_count, final)
            else:
                return LeafNode(node, 0, level_count, final)
        else:
            reference_key_pairs = []

            expect_null = False

            for i in range(0, self.read_capability.block_size, 64):
                ref = node[i : i + 32]
                key = node[i + 32 : i + 64]
                if ref == bytes(32) and key == bytes(32):
                    expect_null = True
                elif expect_null:
                    raise DecodeError("Invalid internal node")
                else:
                    reference_key_pairs.append(ReferenceKeyPair(ref, key))

            return InternalNode(reference_key_pairs, level, 0, level_count, final)

    def _current_node(self):
        return self.path[len(self.path) - 1]

    async def _go_down(self):
        current_node = self._current_node()
        if current_node.level == 0:
            raise ValueError("can not go down from level 0")

        rk_pair = current_node.current_reference_key_pair()

        arity = int(self.read_capability.block_size / 64)
        level_count = (
            (current_node.level_count + current_node.cur) * arity
            if (current_node.level > 1)
            else current_node.level_count + current_node.cur
        )

        node = await self._get_node(
            rk_pair.ref,
            rk_pair.key,
            current_node.level - 1,  # level
            level_count,
            # final
            current_node.final
            and current_node.cur == len(current_node.reference_key_pairs) - 1,
        )

        self.path.append(node)

    def _go_up(self):
        self.path.pop()

    def _go_left(self):
        current_node = self._current_node()
        current_node.cur = current_node.cur - 1

    def _go_right(self):
        current_node = self._current_node()
        if current_node.cur < len(current_node.reference_key_pairs) - 1:
            current_node.cur = current_node.cur + 1
        else:
            raise ValueError("can not go further right")

    def _at_leaf(self):
        current_node = self._current_node()
        return isinstance(current_node, LeafNode)

    def position(self):
        """Return the current stream position."""
        current_node = self._current_node()

        if self._at_leaf():
            return (
                current_node.level_count * self.read_capability.block_size
            ) + current_node.offset
        else:
            return (
                _level_rk_width(self.read_capability.block_size, current_node.level)
                * current_node.level_count
            )

    def _level_range(self):
        current_node = self._current_node()
        if self._at_leaf():
            return current_node.range(self.read_capability.block_size)
        else:
            return current_node.level_range(self.read_capability.block_size)

    def _range(self):
        return self._current_node().range(self.read_capability.block_size)

    def _is_in_level_range(self, offset):
        start, end = self._level_range()
        return start <= offset and offset < end

    def _is_in_range(self, offset):
        start, end = self._range()
        return start <= offset and offset < end

    async def seek(self, offset):
        """Set position to offset."""

        # go up until offset is in range or we have reached root
        while not self._is_in_level_range(offset) and (2 < len(self.path)):
            self._go_up()

        # offset seems to be outside of encoded content, return the current position
        if not self._is_in_level_range(offset):
            return self.position()

        # go down to the correct leaf node
        while not self._at_leaf():
            # go left or right until we are in range
            while not self._is_in_range(offset):
                start, end = self._range()
                if offset < start:
                    self._go_left()
                else:
                    self._go_right()

            # go down at the correct rk-pair
            await self._go_down()

        # we are now at a leaf node
        assert self._at_leaf()

        # set the offset at leaf node
        leaf = self._current_node()
        position = self.position()
        start, end = self._range()
        if offset < end:
            leaf.offset = offset - start
        else:
            leaf.offset = len(leaf.content)

        return self.position()

    async def read(self, size):
        """Read size bytes from the encoded content and return
        them. Fewer than size bytes may be returned if EOF is reached.
        """

        position = self.position()
        out = []
        remaining = size

        # descend to leaf node
        await self.seek(self.position())

        while remaining > 0:
            leaf = self._current_node()
            bytes_from_leaf = leaf.read(remaining)

            out.append(bytes_from_leaf)

            if leaf.final:
                break
            else:
                position = await self.seek(position + len(bytes_from_leaf))
                remaining = remaining - len(bytes_from_leaf)

        return b"".join(out)

    async def readall(self):
        """Read and return all the bytes from the stream from the
        current position until EOF."""
        out = []

        # descend to leaf node
        await self.seek(self.position())

        position = self.position()
        leaf = self._current_node()

        while True:
            bytes_from_leaf = leaf.read(self.read_capability.block_size)
            out.append(bytes_from_leaf)

            if leaf.final:
                break
            else:
                position = await self.seek(position + len(bytes_from_leaf))

            leaf = self._current_node()
        return b"".join(out)
