#!/usr/bin/env python

import argparse
import importlib
import pathlib
import sys
import yaml
import importlib.metadata

from . import context
from .stores import StoreInterface, read_secret


config = {}
no_config_available = True


def load_config():
    global config, no_config_available
    if pathlib.Path(".secenv.yaml").exists():
        config = yaml.load(open(".secenv.yaml", "r"), Loader=yaml.Loader)
    elif pathlib.Path(".secenv.yml").exists():
        config = yaml.load(open(".secenv.yml", "r"), Loader=yaml.Loader)
    else:
        print("Config error: .secenv.yaml not found")
        return

    if config:
        no_config_available = False
    else:
        print("Config error: file is empty")


def parse_args(stores):
    parser = argparse.ArgumentParser()
    subparsers_group = parser.add_subparsers()
    subparsers = {}

    subparsers["version"] = subparsers_group.add_parser(
        "version", help="get secenv version"
    )

    subparsers["contexts"] = subparsers_group.add_parser(
        "contexts", help="list available contexts"
    )

    subparsers["context"] = subparsers_group.add_parser(
        "context", help="generate an environment based on a context"
    )
    subparsers["context"].add_argument("context")
    subparsers["context"].add_argument(
        "-o",
        "--output-format",
        choices=context.available_formats,
        default="shell",
        dest="format",
        help="output format",
    )

    for store in stores:
        type = config["stores"][store]["type"]
        subparsers[store] = subparsers_group.add_parser(
            store,
            help=f"query store '{store}' of type '{type}'",
        )
        stores[store].gen_parser(subparsers[store])

    if len(sys.argv) == 1:
        parser.print_help()
        parser.exit()

    return parser.parse_args()


def find_stores() -> dict[str, StoreInterface]:
    stores = {}
    if "stores" not in config:
        return stores

    for name in config["stores"]:
        infos = config["stores"][name]
        try:
            store = importlib.import_module(
                f".stores.{infos['type']}", package="secenv"
            )
        except ModuleNotFoundError:
            print(f"Config error: no store defined as '{infos['type']}'")
            sys.exit(1)
        stores[name] = store.Store(name, infos)

    return stores


def gen_context(name, stores):
    context_config = config["contexts"][name]
    output = {}

    if context_config is None:
        print(f"Config error: context '{name}' is empty")
        sys.exit(1)

    if "extends" in context_config:
        for extended in context_config["extends"]:
            if extended not in config["contexts"]:
                print(f"Config error: try to extend an unexistent context '{extended}'")
                sys.exit(1)
            if extended == name:
                print(f"Config error: can't extend a context with itself")
                sys.exit(1)
            extended_context = gen_context(extended, stores)
            output.update(extended_context)

    if "vars" in context_config:
        output.update(context.gen_vars(context_config["vars"], stores))

    if "aws_assume_role" in context_config:
        creds = {}
        creds["key_id"] = context_config["aws_assume_role"]["aws_access_key_id"]
        creds["secret_key"] = context_config["aws_assume_role"]["aws_secret_access_key"]
        creds["role"] = context_config["aws_assume_role"]["role_arn"]

        output.update(context.gen_aws_assume_role(creds, stores))

    return output


def list_contexts():
    if "contexts" in config:
        return "\n".join(config["contexts"])
    else:
        return ""


def main():
    if "version" == sys.argv[1]:
        version = importlib.metadata.version("secenv")
        print(f"secenv version {version}")
        sys.exit(0)

    load_config()
    stores = {} if no_config_available else find_stores()
    args = parse_args(stores)

    # remove empty values and 'type' key
    args = {k: v for k, v in vars(args).items() if k != "type" and v}

    if "context" in sys.argv[1]:
        if sys.argv[1].endswith("s"):
            # secenv contexts
            print(list_contexts())
            return

        else:
            # secenv context <ctx>
            context_name = args["context"]
            if "contexts" not in config or context_name not in config["contexts"]:
                print(f"Config error: context '{context_name}' not found")
                sys.exit(1)
            ctx = gen_context(context_name, stores)
            print(context.format_output(ctx, args["format"]))
            return

    else:
        # retrieving a specific secret
        # TODO: replace sys.argv[1] with something more beautiful
        # like from 'args' directly
        store = stores[sys.argv[1]]
        result = read_secret(store, args)
        print(result)
        return


if __name__ == "__main__":
    main()
