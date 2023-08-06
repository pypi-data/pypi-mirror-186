# SPDX-FileCopyrightText: 2023 pukkamustard <pukkamustard@posteo.net>
#
# SPDX-License-Identifier: AGPL-3.0-or-later


"""Cryptographic primitives used by ERIS."""

from Crypto.Hash import BLAKE2b
from Crypto.Cipher import ChaCha20 as ChaCha20_IETF


def Blake2b_256_keyed(input, convergence_secret):
    h_obj = BLAKE2b.new(digest_bits=256, key=convergence_secret)
    h_obj.update(input)
    return h_obj.digest()


def Blake2b_256(input):
    h_obj = BLAKE2b.new(digest_bits=256)
    h_obj.update(input)
    return h_obj.digest()


def ChaCha20(input, key, nonce):
    cipher = ChaCha20_IETF.new(key=key, nonce=nonce)
    return cipher.encrypt(input)


def null_convergence_secret():
    """Returns a null convergence secret (32 bytes of zero)."""
    return bytes(32)
