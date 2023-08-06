import hvac
import hvac.exceptions
from . import StoreInterface


class Store(StoreInterface):
    def __init__(self, name, infos):
        self.name = name
        self.url = super().get_from_config(name, "url", infos)
        self.token = super().get_from_config(name, "token", infos)
        self.client = hvac.Client(url=self.url, token=self.token)

    def gen_parser(self, parser):
        parser.add_argument("secret")
        parser.add_argument("--key")
        parser.add_argument("--engine")

    def read_secret(self, secret, engine=""):
        try:
            read_response = self.client.secrets.kv.read_secret_version(
                path=secret, mount_point=engine
            )
        except hvac.exceptions.InvalidPath as e:
            raise Exception(f"vault store '{self.name}': error during execution: {e}")

        return read_response

    def filter(self, secret, key):
        return secret["data"]["data"][key]
