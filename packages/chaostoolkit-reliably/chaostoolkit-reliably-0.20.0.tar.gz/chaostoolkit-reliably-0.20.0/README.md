# Chaos Toolkit extension for Reliably

![Build](https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/workflows/Build/badge.svg)

[Reliably][reliably] support for the [Chaos Toolkit][chaostoolkit].

[reliably]: https://reliably.com
[chaostoolkit]: http://chaostoolkit.org/

## Install

To be used from your experiment, this package must be installed in the Python
environment where [chaostoolkit][] already lives.

[chaostoolkit]: https://github.com/chaostoolkit/chaostoolkit

```
$ pip install chaostoolkit-reliably
```

## Authentication

To use this package, you must create have registered with Reliably services
through their [CLI][configreliably].

[configreliably]: https://reliably.com/docs/getting-started/login/

You have two ways to pass on the credentials information.

The first one by specifying the path to the Reliably's configuration file,
which defaults to `$HOME/.config/reliably/config.yaml`. The simplest way to
achieve this is by running `$ reliably login` as this will generate the
appropriate file.

```json
{
    "configuration": {
        "reliably_config_path": "~/.config/reliably/config.yaml"
    }
}
```

Because we use the default path, you may omit this configuration's entry
altogether unless you need a specific different path.

The second one is by setting some environment variables as secrets. This is
for specific use case and usually not required.

* `RELIABLY_TOKEN`: the token to authenticate against Reliably's API
* `RELIABLY_ORG`: the Reliably organisation to use
* `RELIABLY_HOST:`: the hostname to connect to, default to `reliably.com`

```json
{
    "secrets": {
        "reliably": {
            "token": {
                "type": "env",
                "key": "RELIABLY_TOKEN"
            },
            "org": {
                "type": "env",
                "key": "RELIABLY_ORG"
            },
            "host": {
                "type": "env",
                "key": "RELIABLY_HOST",
                "default": "reliably.com"
            }
        }
    }
}
```

## Usage

### As Steady Steate Hypothesis

You can use Reliably's SLO as a mechanism to determine if your system has
deviated during a Chaos Toolkit experiment. Here is a simple example:

```json
"steady-state-hypothesis": {
    "title": "We do not consume all of our error budgets during the experiment",
    "probes": [
        {
            "name": "Our 'Must be good' SLO results must be OK",
            "type": "probe",
            "tolerance": true,
            "provider": {
                "type": "python",
                "module": "chaosreliably.slo.probes",
                "func": "slo_is_met",
                "arguments": {
                    "labels": {"name": "must-be-good", "service": "must-be-good-service"},
                    "limit": 5
                }
            },
        }
    ]
}
```

This above example will get the last 5 Objective Results for our `Must be good` SLO and determine if they were all okay or whether we've spent our [error budget](https://sre.google/workbook/error-budget-policy/#:~:text=Error%20budgets%20are%20the%20tool,with%20the%20pace%20of%20innovation.&text=The%20error%20budget%20forms%20a,has%20a%200.1%25%20error%20budget.)
they are allowed.


### As controls

You can use controls provided by `chaostoolkit-reliably` to track your experiments
within Reliably. 

A full example of using the controls is below:

```json
"controls": [
    {
        "name": "chaosreliably",
        "provider": {
            "type": "python",
            "module": "chaosreliably.controls.experiment",
            "arguments": {
                "experiment_ref": "a81c7b966a673190"
            }
        }
    }
],
```

The `experiment_ref` argument is a random string that is used by reliably to
reference this particular experiment. It can be any string but should as
unique as possible to prevent collision. In such case, the experiment would
be overwritten in your organisation.

Once set, you should not change this value or Reliably will not be able to
attach runs to that experiment.

### As Safeguards

Safeguards, provided by the
[Chaos Toolkit addons extension](https://github.com/chaostoolkit/chaostoolkit-addons)
gives you a nice way to interrupt an experiment as soon as error budgets have
been consumed. This is orthogonal to the steady-state hypothesis as it is a
mechanism to protect your system from being harmed too harshly by an experiment.

```json
"controls": [
    {
        "name": "safeguard",
        "provider": {
            "type": "python",
            "module": "chaosaddons.controls.safeguards",
            "arguments": {
                "probes": [
                    {
                        "name": "we-do-not-have-enough-error-budget-left-to-carry-on",
                        "type": "probe",
                        "frequency": 5,
                        "provider": {
                            "type": "python",
                            "module": "chaosreliably.slo.probes",
                            "func": "slo_is_met",
                            "arguments": {
                                "labels": {"name": "must-be-good", "service": "must-be-good-service"},
                                "limit": 5
                            }
                        },
                        "tolerance": true
                    }
                ]
            }
        }
    }
]
```

As you can notice it is the same construct as for the steady-state, it's merely
used with a different purpose. Here these probes will be executed every 5s
during the experiment (this frequence is for demo purposes, you would usually only run it
once every minute or less).

## Contribute

From a code perspective, if you wish to contribute, you will need to run a
Python 3.6+ environment. Please, fork this project, write unit tests to cover
the proposed changes, implement the changes, ensure they meet the formatting
standards set out by `black`, `flake8`, `isort`, and `mypy`, add an entry into
`CHANGELOG.md`, and then raise a PR to the repository for review

Please refer to the [formatting](#formatting-and-linting) section for more
information on the formatting standards.

The Chaos Toolkit projects require all contributors must sign a
[Developer Certificate of Origin][dco] on each commit they would like to merge
into the master branch of the repository. Please, make sure you can abide by
the rules of the DCO before submitting a PR.

[dco]: https://github.com/probot/dco#how-it-works

### Develop

If you wish to develop on this project, make sure to install the development
dependencies. But first, [create a virtual environment][venv] and then install
those dependencies.

[venv]: http://chaostoolkit.org/reference/usage/install/#create-a-virtual-environment

```console
$ make install-dev
```

### Test

To run the tests for the project execute the following:

```console
$ make tests
```

### Formatting and Linting

We use a combination of [`black`][black], [`flake8`][flake8], [`isort`][isort],
and [`mypy`][mypy] to both lint and format this repositories code.

[black]: https://github.com/psf/black
[flake8]: https://github.com/PyCQA/flake8
[isort]: https://github.com/PyCQA/isort
[mypy]: https://github.com/python/mypy

Before raising a Pull Request, we recommend you run formatting against your
code with:

```console
$ make format
```

This will automatically format any code that doesn't adhere to the formatting
standards.

As some things are not picked up by the formatting, we also recommend you run:

```console
$ make lint
```

To ensure that any unused import statements/strings that are too long, etc.
are also picked up. It will also provide you with any errors `mypy` picks up.
