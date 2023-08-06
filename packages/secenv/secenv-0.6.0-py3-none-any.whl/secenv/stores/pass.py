import passpy
from . import StoreInterface


class Store(StoreInterface):
    def __init__(self, name, infos):
        self.name = name
        directory = super().get_from_config(
            name, "directory", infos, default="~/.password-store"
        )
        self.store = passpy.Store(store_dir=directory)

    def gen_parser(self, parser):
        parser.add_argument("secret")

    def read_secret(self, secret):
        if res := self.store.get_key(secret):
            return res
        else:
            raise Exception(f"Secret '{secret}' not found in store '{self.name}'")
