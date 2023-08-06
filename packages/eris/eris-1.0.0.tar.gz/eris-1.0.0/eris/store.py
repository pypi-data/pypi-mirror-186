# SPDX-FileCopyrightText: 2022 Endo Renberg
# SPDX-FileCopyrightText: 2023 pukkamustard <pukkamustard@posteo.net>
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from enum import Enum, auto
from asyncio import *
from aiocoap import *
from Crypto.Cipher import ChaCha20

from eris import base32


class Store:
    """Stores blocks of encoded content"""

    async def get(self, ref, block_size=False):
        """Gets the block with given reference.

        Optionally a size may be provided (e.g. block_size=1024 or
        size=32768). This may be used by the store to optimize block
        access."""
        raise NotImplementedError()

    async def put(self, ref, block):
        """Stores a block"""
        raise NotImplementedError()

    async def close(self):
        """Closes connection to the store"""
        pass


class NullStore(Store):
    """A store that does not store anything.

    Useful if you want to compute the ERIS read capability without
    storing blocks anywhere.

    """

    async def get(self, ref, block_size=False):
        False

    async def put(self, ref, block):
        True


class DictStore(Store):
    """A in-memory store using a Python dict"""

    def __init__(self):
        self.dict = dict()

    async def get(self, ref, block_size=False):
        if ref in self.dict:
            return self.dict[ref]
        else:
            False

    async def put(self, ref, block):
        self.dict[ref] = block
