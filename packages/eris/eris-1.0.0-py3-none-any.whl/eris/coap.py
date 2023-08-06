# SPDX-FileCopyrightText: 2022 Endo Renberg
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import eris
from eris import base32
from eris import crypto
import aiocoap
import aiocoap.resource as resource


class Store(eris.Store):
    """A ERIS store that is connected via CoAP"""
    def __init__(self, url):
        """
        Initialize connection to CoAP store.

        :param str url: Store URL (e.g. 'coap+tcp://example.net/.well-known/eris')
        """
        self.url = url
        self.context = None

    async def get(self, ref, block_size=False):

        # init context
        if self.context is None:
            self.context = await aiocoap.Context.create_client_context()

        msg = aiocoap.Message(code=aiocoap.GET, uri=self.url)
        msg.opt.uri_path += ("blocks",)
        msg.opt.uri_query += (base32.encode(ref),)  # should be binary
        if block_size:
            msg.opt.size1 = block_size

        response = await self.context.request(msg).response
        if response.code != aiocoap.CONTENT:
            return False
        else:
            return response.payload

    async def put(self, ref, block):
        # init context
        if self.context is None:
            self.context = await aiocoap.Context.create_client_context()

        msg = aiocoap.Message(code=aiocoap.PUT, uri=self.url, payload=block)
        msg.opt.uri_path += ("blocks",)

        response = await self.context.request(msg, handle_blockwise=False).response
        if response.code != aiocoap.CREATED:
            raise KeyError(response.code)

    async def close(self):
        if self.context is not None:
            await self.context.shutdown()


class BlocksResource(resource.Resource):
    """ERIS CoAP store `blocks` resource"""

    def __init__(self, store):
        super().__init__()
        self.store = store

    async def render_get(self, request):
        for ref in request.opt.uri_query:
            ref = ref if isinstance(ref, bytes) else base32.decode(ref)
            block = await self.store.get(ref)
            if block:
                return aiocoap.Message(code=aiocoap.CONTENT, payload=block)
            else:
                return aiocoap.Message(code=aiocoap.NOT_FOUND)

    async def render_put(self, request):
        block = request.payload
        if isinstance(block, bytes) and len(block) in [1024, 32768]:
            ref = crypto.Blake2b_256(block)
            try:
                await self.store.put(ref, block)
                return aiocoap.Message(code=aiocoap.CREATED)
            except NotImplementedError:
                return aiocoap.Message(code=aiocoap.NOT_FOUND)
        else:
            return aiocoap.Message(code=aiocoap.BAD_REQUEST)


def add_store_resources(site, store, path=[".well-known", "eris"]):
    """Adds CoAP resources to implement an ERIS CoAP store

    :param aiocoap.resource.Site site: Site to add resources to.
    :param eris.Store store: Underlying block store.
    :param list(str) path: URL path to ERIS CoAP store (defaults to `['.well-known', 'eris']`).
    """
    site.add_resource(path + ["blocks"], BlocksResource(store))
