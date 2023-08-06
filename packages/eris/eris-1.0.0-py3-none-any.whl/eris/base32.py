# SPDX-FileCopyrightText: 2023 pukkamustard <pukkamustard@posteo.net>
#
# SPDX-License-Identifier: AGPL-3.0-or-later

""" Utility functions for working with Base32."""

import base64


def decode(s):
    """Returns the bytes encoded as Base32 in [s]."""
    last_block_width = len(s) % 8
    if last_block_width != 0:
        s += (8 - last_block_width) * "="
    return base64.b32decode(s)


def encode(b):
    """Returns the unpadded Base32 encoding of [b]."""
    return base64.b32encode(b).decode().rstrip("=")
