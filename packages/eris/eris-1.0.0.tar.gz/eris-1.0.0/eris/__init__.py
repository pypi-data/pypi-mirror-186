# SPDX-FileCopyrightText: 2022 pukkamustard <pukkamustard@posteo.net>
#
# SPDX-License-Identifier: AGPL-3.0-or-later

"""ERIS for Python"""

from eris.read_capability import ReadCapability
from eris.store import Store, NullStore, DictStore
from eris.encoder import Encoder
from eris.decoder import Decoder

from eris.crypto import null_convergence_secret


def spec_version():
    """Returns the version of the ERIS specification implemented"""
    return "1.0.0"
