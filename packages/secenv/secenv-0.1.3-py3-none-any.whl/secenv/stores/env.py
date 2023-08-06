import os
from . import StoreInterface


class Store(StoreInterface):
    def __init__(self, name, infos):
        pass

    def gen_parser(self, parser):
        parser.add_argument("secret")

    def read_secret(self, secret):
        return os.getenv(secret)
