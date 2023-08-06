import argparse
import os
from abc import ABC, abstractmethod


EnvPrefix = "SECENV"

def read_secret(store, args):
    key = None
    if "key" in args:
        key = args["key"]
        del args["key"]

    secret = store.read_secret(**args)
    if key:
        return store.filter(secret, key)
    else:
        return secret


class StoreInterface(ABC):
    @abstractmethod
    def __init__(self, name: str, infos: dict) -> None:
        """Init the store, check the provided keys, and create possible client"""
        pass

    def get_from_config(self, store: str, value: str, infos: dict, default="") -> str:
        if value not in infos and f"{EnvPrefix}_{store}_{value}" not in os.environ:
            if not default:
                raise Exception(
                    f"Config error: '{value}' is required in store '{store}' or {EnvPrefix}_{store}_{value} in env"
                )
            else:
                return default
        return infos.get(
            value,
            os.getenv(f"{EnvPrefix}_{store}_{value}"),
        )

    @abstractmethod
    def gen_parser(self, parser: argparse.ArgumentParser) -> None:
        """Generate the parser that reads the arguments and options"""
        pass

    @abstractmethod
    def read_secret(self, secret: str) -> str:
        """Read a secret from the desired password store"""
        pass
