import sys
import threading
from .stores import read_secret
from .contexts.aws_assume_role import aws_assume_role
from .utils import escape


available_formats = ["dotenv", "shell"]


def format_output(context, format):
    output = []
    if format == "dotenv":
        for k, v in context.items():
            output.append(f"{k}={escape(v)}")
        output = "\n".join(output)
    elif format == "shell":
        for k, v in context.items():
            output.append(f"export {k}={escape(v)}")
        output = "\n".join(output)
    else:
        print(f"User error: format {format} not found, available: {available_formats}")
        sys.exit(1)
    return str(output)


def _handle_var(key, value, stores, output={}):
    if type(value) == str:
        # raw value
        output[key] = value

    else:
        # retrieve from store
        store = value["store"]
        if store not in stores:
            print(f"Config error: store '{store}' not found in config")
            sys.exit(1)

        value = {k: v for k, v in value.items() if k != "store" and v}
        res = read_secret(stores[store], value)
        output[key] = res


def gen_vars(vars, stores):
    output = {}
    threads = []

    for key, value in vars.items():
        t = threading.Thread(target=_handle_var, args=[key, value, stores, output])
        t.start()
        threads.append(t)
    list(map(lambda t: t.join(), threads))

    return output


def gen_aws_assume_role(creds, stores):
    output = {}

    for k, v in creds.items():
        # raw values are passed directly
        if type(v) == str:
            continue
        # and values from stores are computed first
        args = {k2: v2 for k2, v2 in v.items() if k2 != "store" and v2}
        creds[k] = read_secret(stores[v["store"]], args)

    try:
        key_id, secret_key, token = aws_assume_role(
            creds["key_id"], creds["secret_key"], creds["role"]
        )
        output["AWS_ACCESS_KEY_ID"] = key_id
        output["AWS_SECRET_ACCESS_KEY"] = secret_key
        output["AWS_SESSION_TOKEN"] = token
    except:
        print(f"AWS error: couldn't assume role '{creds['role']}'")
        sys.exit(1)

    return output
