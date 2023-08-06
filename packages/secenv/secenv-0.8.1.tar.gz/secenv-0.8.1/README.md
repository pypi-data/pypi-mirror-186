# secenv

`secenv` is an utility program to list and read secrets from multiple stores.
It also defines contexts, and generates the associated environment values.

Instead of remembering how to use each store CLI, learn to use `secenv` and forget about them.

Instead of switching secrets between each environment, learn to use `secenv` and switch automatically.

For now, `secenv` can read secrets from:

- AWS SecretsManager, using the `boto3` library
- Bitwarden, using the `rbw` unofficial CLI (it is planned to migrate to plain Python)
- Environment, using `os.getenv`
- GNU Pass, using the `passpy` library
- Hashicorp Vault, using the `hvac` library


## Table of contents

- [secenv](#secenv)
  - [Table of contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Defining stores](#defining-stores)
    - [Querying the stores](#querying-the-stores)
    - [Defining contexts](#defining-contexts)
      - [Extending contexts](#extending-contexts)
      - [AWS Assume Role](#aws-assume-role)
      - [Output format](#output-format)
    - [Integration with `direnv`](#integration-with-direnv)
  - [Development](#development)
    - [Adding a store](#adding-a-store)


## Installation

```sh
# from PyPI
pip install secenv

# from sources
git clone https://gitlab.com/keltiotechnology/keltio-products/secenv
cd secenv && pip install .
```

## Usage

`secenv` is driven by a `.secenv.yaml` (or `.yml`) configuration file.


### Defining stores

This file defines *stores*, like Bitwarden or Vault.

> Note that each field of the stores below have to be defined.

```yaml
stores:
  client_vault:
    type: vault
    url: https://vault.client.com
    token: hvs.ThIsIsAS3cUr3T0K3N

  bitwarden_instance:
    type: bitwarden
    url: https://bitwarden.ourcompany.com
    user: user
    password: password

  aws_account:
    type: aws
    region: eu-west-3
    access_key_id: AKIASP2TPHJS5TULPFF3
    secret_access_key: 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

  local:
    type: env

  pass_folder:
    type: pass
    # optional, default is ~/.password-store
    directory: /path/to/folder
```

> Note that the variables can be defined using ENV values like this: `SECENV_<store>_<variable>` (e.g. `SECENV_aws_account_region`).


### Querying the stores

Once the stores created, it is possible to query them, by example:

```sh
$ secenv client_vault --engine accesses github --key username
my_user

$ secenv bitwarden_instance client/aws_access_key_id
AKIAAZDKAZLMQSKD1234

$ secenv aws_account DATABASE_CREDS --key username
db_user

$ secenv local HOME
/Users/user

$ secenv pass_folder ssh/bastion_ssh_pubkey
ssh-rsa bliblablou...
```

> The `--key` argument is optional, and is used if the output is a Key/Value store (like JSON).


### Defining contexts

Now that the core concepts of `secenv` are defined, see how we can define *contexts*, which are a set of keys injected in an environment.

```yaml
contexts:
  dev:
    vars:
      # passed directly to the environment
      URL: dev.example.com

      # queried from the store
      GITHUB_USERNAME:
        store: client_vault
        engine: accesses
        secret: github
        key: username

      AWS_ACCESS_KEY_ID:
        store: bitwarden_instance
        secret: client/aws_access_key_id

      DATABASE_USERNAME:
        store: aws_account
        secret: DATABASE_CREDS
        key: username

      HOME:
        store: env
        secret: HOME

      SSH_PUBKEY:
        store: pass_folder
        secret: ssh/bastion_ssh_pubkey
```

Get the available contexts by running:

```
> secenv contexts
dev
```

And generate a context by running:

```
> secenv context dev
export URL='dev.example.com'
export GITHUB_USERNAME='my_user'
export AWS_ACCESS_KEY_ID='AKIAAZDKAZLMQSKD1234'
export DATABASE_USERNAME='username'
export HOME='/Users/user'
export SSH_PUBKEY='ssh-rsa bliblablou...'
```


#### Extending contexts

It is possible, for a context, to extend another one.
To do so, use the `extends` keyword as below:

```yaml
contexts:
  default:
    vars:
      VAR: value
  dev:
    extends:
      - default
```

Then:

```
> secenv context dev
export VAR='value'
```

A context can extend more than one other.
The latest takes precedence over the first.

This means, in the example above, that if a context define a `VAR` variable and is extended below `default`, the the value of `VAR` will get overwritten.
Then, if `dev` defines `VAR` as well, its value will stay and overwrite the formers.


#### AWS Assume Role

It is possible as well to generate AWS keys to assume a role on a sub-account.
Add it this way:

```yaml
contexts:
  dev:
    aws_assume_role:
      # value can be a raw string or queried from a store
      aws_access_key_id: AKIASP2TPHJS5TULPFF3
      aws_secret_access_key:
        store: bitwarden_instance
        secret: client/aws_secret_access_key
      role_arn:
        store: client_vault
        engine: accesses
        secret: aws
        key: dev_role_arn
```

Generating the `dev` context will add 3 variables, being the AWS access key ID, the associated private access key, and a role token.


#### Output format

By default, `secenv context <ctx>` generates an output that can be `eval`-ed (i.e. `eval $(secenv context <ctx>)`).
Other output formats are available using the `--output-format` option of the `context` command.


### Integration with `direnv`

The ultimate goal of `secenv` is to automate context switching between several projects.
If `direnv` is installed on local system, it is possible to integrate `secenv` this way:

```sh
# .secenv.yaml
...as above

# .envrc

echo "which context?"
select env in $(secenv contexts); do eval $(secenv context "$env"); break; done
```

The variables defined in the `contexts.dev.envs` block are now exported in th environment.


## Development

To install the required dependencies for development, run:

```
pip install secenv[dev]
```

### Adding a store

The stores are defined in the `secenv/stores` directory. They implement the `StoreInterface` defined in `__init__.py`.

The `StoreInterface.get_from_config` function permits to read a value from the config file, or from the environment directly.
This function takes an optional argument, `default`.

If the wanted value is not in neither the config file, nor the environment, then the `default` value is returned if one is provided.
If there is no `default` value, then an exception is raised.

If the secret can be a key-value store, a `--key` option can be added to the parser (see AWS and Vault stores as they implement this).
The new store must provide a `Store.filter(secret, key)` function.
