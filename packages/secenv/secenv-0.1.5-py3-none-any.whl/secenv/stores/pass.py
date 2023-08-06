import passpy
from . import StoreInterface


class Store(StoreInterface):
    def __init__(self, name, infos):
        directory = super().get_from_config(
            name, "directory", infos, default="~/.password-store"
        )
        self.store = passpy.Store(store_dir=directory)

    def gen_parser(self, parser):
        parser.add_argument("secret")

    def read_secret(self, secret):
        return self.store.get_key(secret)
