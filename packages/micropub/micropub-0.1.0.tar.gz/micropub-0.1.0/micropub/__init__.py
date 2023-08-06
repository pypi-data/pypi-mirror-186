"""
A Micropub client.

A [Micropub](https://micropub.spec.indieweb.org) server is used to manage content
on your website (ie. posts at permalinks). A Micropub client is used to perform
content management operations on these posts (eg. create/read/update/delete).

"""

import functools

import requests
import rich.progress
from requests_toolbelt.multipart.encoder import MultipartEncoder
from tqdm import tqdm
from tqdm.utils import CallbackIOWrapper


class PostNotCreated(Exception):
    """Post failed to be created."""


class Client:
    """Micropub client."""

    def __init__(self, endpoint, access_token=None):
        """Initiate a session with the Micropub server."""
        self.session = requests.session()
        self.endpoint = endpoint
        self.access_token = access_token
        self.session.headers.update(Authorization=f"Bearer {access_token}")
        self.get = functools.partial(self.session.get, endpoint)
        self.post = functools.partial(self.session.post, endpoint)

    def get_post(self, permalink):
        """Get the post at `permalink`."""
        return self.get(params={"q": "source", "url": permalink})

    def create_post(self, properties, h="entry"):
        """Create a post of type `h` with given `properties`."""
        response = self.post(json={"type": [f"h-{h}"], "properties": dict(properties)})
        if response.status_code != 201:
            raise PostNotCreated()
        return response.url, response.links


class MediaClient:
    """Micropub media client."""

    def __init__(self, endpoint, access_token=None):
        """Initiate a session with the Micropub server."""
        self.session = requests.session()
        self.endpoint = endpoint
        self.access_token = access_token
        self.session.headers.update(Authorization=f"Bearer {access_token}")

    def upload(self, filepath):
        """Return URL of uploaded `filepath`."""
        # with filepath.open("rb") as fp:
        #     with tqdm(
        #         total=filesize, unit="B", unit_scale=True, unit_divisor=1024
        #     ) as progress:
        #         wrappedfile = CallbackIOWrapper(progress.update, fp, "read")
        #         response = self.session.post(self.endpoint, files={"file": wrappedfile})
        # with rich.progress.open(filepath, "rb") as fp:
        #     m = MultipartEncoder(fields={"file": (filepath.name, fp)})
        #     response = self.session.put(
        #         self.endpoint, data=m, headers={"Content-Type": m.content_type}
        #     )
        # with rich.progress.open(filepath, "rb") as fp:
        #     response = self.session.post(self.endpoint, files={"file": fp})
        filesize = filepath.stat().st_size
        with rich.progress.open(filepath, "rb") as fp:
            location = self.session.post(
                self.endpoint, json={"name": filepath.name, "size": filesize}
            ).headers["Location"]
            index = 0
            while True:
                chunk = fp.read(5000000)
                if not chunk:
                    break
                offset = index + len(chunk)
                self.session.put(
                    location,
                    data=chunk,
                    headers={
                        "Content-Type": "application/octet-stream",
                        "Content-Range": f"bytes {index}-{offset}/{filesize}",
                    },
                )
                index = offset
        return location
