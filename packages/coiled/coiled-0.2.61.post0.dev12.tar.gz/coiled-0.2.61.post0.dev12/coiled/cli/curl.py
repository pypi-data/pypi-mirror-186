import click

import coiled

from .utils import CONTEXT_SETTINGS


@click.command(
    context_settings=CONTEXT_SETTINGS,
    help="CLI to hit endpoints using Coiled account authentication (mostly for internal use)",
)
@click.argument("url")
@click.option("-X", "--request", default="GET")
@click.option("-d", "--data", multiple=True)
def curl(url: str, request, data):
    all_data = "&".join(data) if data else None
    with coiled.Cloud() as cloud:

        if "http" not in url:
            url = f"{cloud.server}{url}"

        response = sync_request(cloud, url, method=request, data=all_data)
    print(response)


def sync_request(cloud, url, method, data):
    response = cloud._sync(
        cloud._do_request,
        method=method,
        url=url,
        data=data,
    )
    if response.status >= 400:
        print(f"{url} returned {response.status}")

    async def get_text(r):
        return await r.text()

    return cloud._sync(
        get_text,
        response,
    )
