![DASF Logo](https://git.geomar.de/digital-earth/dasf/dasf-messaging-python/-/raw/master/docs/_static/dasf_logo.svg)

[![DOI](https://git.geomar.de/digital-earth/dasf/dasf-messaging-python/-/raw/master/doi_badge.svg)](https://doi.org/10.5880/GFZ.1.4.2021.005)
[![PyPI version](https://badge.fury.io/py/demessaging.svg)](https://badge.fury.io/py/demessaging)
[![status](https://joss.theoj.org/papers/e8022c832c1bb6e879b89508a83fa75e/status.svg)](https://joss.theoj.org/papers/e8022c832c1bb6e879b89508a83fa75e)

## dasf-messaging-python

`DASF: Messaging Python` is part of the Data Analytics Software Framework (DASF, https://git.geomar.de/digital-earth/dasf),
developed at the GFZ German Research Centre for Geosciences (https://www.gfz-potsdam.de).
It is funded by the Initiative and Networking Fund of the Helmholtz Association through the Digital Earth project
(https://www.digitalearth-hgf.de/).

`DASF: Messaging Python` is a RPC (remote procedure call) wrapper library for the python programming language. As part of the data analytics software framework DASF, it implements the DASF RPC messaging protocol. This message broker based RPC implementation supports the integration of algorithms and methods implemented in python in a distributed environment. It utilizes pydantic (https://pydantic-docs.helpmanual.io/) for data and model validation using python type annotations. DASF distributes messages via a central message broker. Currently we support a self-developed message broker called dasf-broker-django, as well as an ‘off-the-shelf’ solution called Apache Pulsar. (also see: [Message Broker](https://digital-earth.pages.geomar.de/dasf/dasf-messaging-python/developers/messaging.html#messagebroker))

---

### Service Desk

For everyone without a Geomar Gitlab account, we setup the Service Desk feature for this repository.
It lets you communicate with the developers via a repository specific eMail address. Each request will be tracked via the Gitlab issuse tracker.
In order to send a follow-up message, simply reply to the corresponding notification eMail.

eMail: [gitlab+digital-earth-dasf-dasf-messaging-python-1576-issue-@git-issues.geomar.de](mailto:gitlab+digital-earth-dasf-dasf-messaging-python-1576-issue-@git-issues.geomar.de)

### Documentation

see: https://digital-earth.pages.geomar.de/dasf/dasf-messaging-python/

#### PyPI Package `demessaging` 
[![PyPI version](https://badge.fury.io/py/demessaging.svg)](https://badge.fury.io/py/demessaging)

`DASF: Messaging Python` is released as a PyPI package called `demessaging`. 

You may install it via:

```bash 
pip install demessaging[backend]
```

#### **Source Code Examples**
see: https://git.geomar.de/digital-earth/dasf/dasf-messaging-python/-/blob/master/ExampleMessageConsumer.py

- generate the counterpart via `python ExampleMessageConsumer.py generate > ExampleMessageProducerGen.py`
- call the consumer module via the generated producer,
see https://git.geomar.de/digital-earth/dasf/dasf-messaging-python/-/blob/master/ExampleMessageProducer.py


#### **Howto make the docs**

First, make sure you have [graphviz](https://www.graphviz.org/download/)
installed, and run `pip install -r docs/requirements.txt`.

Then change directories into the `docs` subfolder and execute

```bash
make html
```

The built HTML documentation can be access via `docs/_build/html/index.html`.





### Contributing

> We are working on a more detailed contributing guide, but here is the short
> version:

When you want to contribute to the code, please do clone the source code
repository and install it with the `[dev]` extra, i.e.

```bash
git clone https://git.geomar.de/digital-earth/dasf/dasf-messaging-python.git
cd dasf-messaging-python
pip install -e .[dev]
```
We use automated formatters (see their config in `pyproject.toml` and
`setup.cfg`), namely

-   [Black](https://black.readthedocs.io/en/stable/) for standardized
    code formatting
-   [blackdoc](https://blackdoc.readthedocs.io/en/stable/) for
    standardized code formatting in documentation
-   [Flake8](http://flake8.pycqa.org/en/latest/) for general code
    quality
-   [isort](https://github.com/PyCQA/isort) for standardized
    order in imports.
-   [mypy](http://mypy-lang.org/) for static type checking on [type
    hints](https://docs.python.org/3/library/typing.html)

We highly recommend that you setup [pre-commit hooks](https://pre-commit.com/)
to automatically run all the above tools every time you make a git commit. This
can be done by running

```
pre-commit install
```

from the root of the repository. You can skip the pre-commit checks
with ``git commit --no-verify`` but note that the CI will fail if it encounters
any formatting errors.

You can also run the pre-commit step manually by invoking

```
pre-commit run --all-files
```

#### Running the test suite

Tests can be run via `tox`. Install `tox` via `pip install tox` and simply run

```
tox
```

from the root of the repository.

### Recommended Software Citation

`Eggert, Daniel; Sommer, Philipp; Dransch, Doris (2021): DASF: Messaging Python: A python RPC wrapper for the data analytics software framework. GFZ Data Services. https://doi.org/10.5880/GFZ.1.4.2021.005`


### License
```
Copyright 2021 Helmholtz Centre Potsdam GFZ German Research Centre for Geosciences, Potsdam, Germany / DASF Data Analytics Software Framework

Licensed under the Apache License, Version 2.0 (the "License");
you may not use these files except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

### Contact
Dr.-Ing. Daniel Eggert  
eMail: <daniel.eggert@gfz-potsdam.de>


Helmholtz Centre Potsdam GFZ German Research Centre for Geoscienes  
Section 1.4 Remote Sensing & Geoinformatics  
Telegrafenberg  
14473 Potsdam  
Germany
