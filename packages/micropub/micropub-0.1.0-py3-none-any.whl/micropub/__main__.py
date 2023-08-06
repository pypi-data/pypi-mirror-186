"""A Micropub client."""

import json
import pathlib

import indieauth
import txt
import webcli
from rich.console import Console

import micropub

__all__ = ["main"]

main = txt.application("micropub", micropub.__doc__)
console = Console()
site_url_path = pathlib.Path("~/.website").expanduser()
token_path = pathlib.Path("~/.micropub").expanduser()


@main.register()
class Post:
    """A post."""

    def setup(self, add_arg):
        add_arg("endpoint", help="address of the Micropub endpoint")
        add_arg("--type", default="entry", help="post type")
        add_arg("--token", default=None, help="IndieAuth bearer token")
        add_arg("--channel", nargs="*", help="add to given channel(s)")

    def run(self, stdin, log):
        if self.token is None:
            device_endpoint = "https://ragt.ag/auth/devices"
            token_endpoint = "https://ragt.ag/auth/tokens"
            device_response = indieauth.request_device_token(
                device_endpoint, "Python-Micropub CLI"
            )
            token_response = indieauth.poll_device_token(
                token_endpoint, device_response
            )
            self.token = token_response.json["access_token"]
            print(self.token)
        properties = json.loads(stdin.read())
        # try:
        #     properties["channel"].extend(self.channel)
        # except KeyError:
        #     if self.channel:
        #         properties["channel"] = self.channel
        client = micropub.Client(self.endpoint, self.token)
        location, links = client.create_post(properties, h=self.type)
        print("Location:", location)
        if links:
            print("Links:", links)
        return 0


@main.register()
class Media:
    """A media upload."""

    def setup(self, add_arg):
        # XXX add_arg("endpoint", help="address of the MP endpoint")
        # XXX add_arg("token", help="token for the MP endpoint")
        add_arg("path", help="path of file to upload", type=pathlib.Path)

    def run(self, stdin, log):
        with site_url_path.open() as fp:
            endpoint = webcli.get(fp.read()).link("media-endpoint")
        with token_path.open() as fp:
            token = fp.read().strip()
        client = micropub.MediaClient(endpoint, token)
        if self.path.is_dir():
            files = list(self.path.iterdir())
        else:
            files = [self.path]
        # with console.status("[bold cyan]uploading files"):
        for filepath in files:
            location = client.upload(filepath)
            print(filepath, "⟶  ", location)
            # console.print(filepath, "⟶  ", location)
        return 0


if __name__ == "__main__":
    main()

# nuitka-project: --include-package-data=mf2py
