# SPDX-FileCopyrightText: 2022 pukkamustard <pukkamustard@posteo.net>
#
# SPDX-License-Identifier: AGPL-3.0-or-later


import struct
from eris import base32


class ReadCapability:
    """An ERIS read capability."""

    def _of_bytes(self, b):
        return struct.unpack("BB32s32s", b)

    def _of_string(self, urn):
        if urn.startswith("urn:eris:"):
            return self._of_bytes(base32.decode(urn[9:]))
        else:
            raise ValueError("not a valid ERIS read capability")

    def __repr__(self):
        return "<eris.ReadCapability block_size:{} level:{}, root_ref:{}, root_key: {}>".format(
            self.block_size,
            self.level,
            self.root_ref,
            self.root_key,
        )

    def __bytes__(self):

        block_size_byte = 0x00

        if self.block_size == 1024:
            block_size_byte = bytes([0x0A])
        elif self.block_size == 32768:
            block_size_byte = bytes([0x0F])
        else:
            raise ValueError("invalid block size")

        return block_size_byte + bytes([self.level]) + self.root_ref + self.root_key

    def __str__(self):
        read_cap = base32.encode(bytes(self))
        return "urn:eris:" + read_cap

    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            block_size, level, root_ref, root_key = self._of_string(args[0])
            self.block_size = 2**block_size
            self.level = level
            self.root_ref = root_ref
            self.root_key = root_key
        elif len(args) == 1 and isinstance(args[0], bytes):
            block_size, level, root_ref, root_key = self._of_bytes(args[0])
            self.block_size = 2**block_size
            self.level = level
            self.root_ref = root_ref
            self.root_key = root_key
        elif len(args) == 4:
            if args[0] != 1024 and args[0] != 32768:
                raise ValueError("invalid block size")
            self.block_size = args[0]
            self.level = args[1]
            self.root_ref = args[2]
            self.root_key = args[3]
