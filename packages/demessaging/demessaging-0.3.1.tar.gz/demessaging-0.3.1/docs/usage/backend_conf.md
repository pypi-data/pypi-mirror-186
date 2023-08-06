(config-parameters)=
# Backend module configuration parameters

You have three possibilities to configure the backend module. You can include
them in the code via the [`main` function](config-main), provide them as
[command-line arguments](config-cli) or [use environment variables](config-env).

```{note}
Command line arguments take precedence over parameters to the `main` function
which in turn takes precendece over environment variables!
```

(config-main)=
## Using the main function

When calling the {func}`~demessaging.backend.main` function, you can pass
provide various options to call for configuration (see the
{func}`API reference <demessaging.backend.main>`).

(config-cli)=
## Providing command line arguments

All parameters can also be provided via command line arguments.

```{argparse}
:module: demessaging.cli
:func: get_parser
:prog: python my_module.py
```

(config-env)=
## Using environment variables

Parameters for the messaging config (i.e. for
{class}`~demessaging.config.PulsarConfig` and
{class}`~demessaging.config.WebsocketURLConfig`) can also be provided via
environment variables. Add the following prefix to the exported parameter:
`DE_BACKEND_`, e.g. `DE_BACKEND_HOST` to set the `host` parameter.
