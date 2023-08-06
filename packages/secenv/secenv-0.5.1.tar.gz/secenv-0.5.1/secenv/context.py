import sys
from .contexts.aws_assume_role import aws_assume_role
from .utils import escape


available_formats = ["shell"]  # ["dotenv", "shell"]


def format_output(context, format):
    output = []
    # TODO: check escaping in .env file before
    # if format == "dotenv":
    #     for k, v in context.items():
    #         output.append(f"{k}={escape(v)}")
    #     output = "\n".join(output)
    if format == "shell":
        for k, v in context.items():
            output.append(f"export {k}={escape(v)}")
        output = "\n".join(output)
    else:
        print(f"User error: format {format} not found, available: {available_formats}")
    return str(output)


def gen_vars(vars, stores):
    output = {}
    for key, value in vars.items():
        if type(value) == str:
            # raw value
            output[key] = value
        else:
            # get from secrets
            store = value["store"]
            if store not in stores:
                print(f"Config error: store '{store}' not found in config")
                sys.exit(1)

            value = {k: v for k, v in value.items() if k != "store" and v}
            res = stores[store].read_secret(**value)
            output[key] = res

    return output


def gen_aws_assume_role(creds, stores):
    output = {}

    for k, v in creds.items():
        # raw values are passed directly
        if type(v) == str:
            continue
        # and values from stores are computed first
        args = {k2: v2 for k2, v2 in v.items() if k2 != "store" and v2}
        creds[k] = stores[v["store"]].read_secret(**args)

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
