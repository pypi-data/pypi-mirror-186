"""Sending async requests to OpenAPI for increased performance."""

import asyncio
from pprint import pprint
from typing import List

from httpx import Response

from saxo_apy import SaxoOpenAPIClient

client = SaxoOpenAPIClient()
client.login()  # ensure app_config.json is available in this directory


async def main() -> List[Response]:
    """Create API requests and await."""
    # take care with the amount of requests here - OpenAPI will block excessive calls
    requests = [client.aget(path) for path in ["/port/v1/clients/me", "/port/v1/accounts/me", "/port/v1/users/me"]]
    results = await asyncio.gather(*requests)
    return results


results = client.async_loop.run_until_complete(main())

for result in results:
    # print all client, account, and user data to the command line
    pprint(result)
