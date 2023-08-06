# Welcome to DASF's documentation!

![DASF Logo](/_static/dasf_logo_v2_640.png)

The **D**ata **A**nalytics **S**oftware **F**ramework DASF supports scientists to conduct data analysis in distributed IT infrastructures by sharing data analysis tools and data. For this purpose, DASF defines a remote procedure call (RPC) messaging protocol that uses a central message broker instance. Scientists can augment their tools and data with this protocol to share them with others or re-use them in different contexts.

## Language support
The DASF RPC messaging protocol is based on JSON and uses Websockets for the underlying data exchange. Therefore the DASF RPC messaging protocol in general is language agnostic, so all languages with Websocket support can be utilized. As a start DASF provides two ready-to-use language bindings for the messaging protocol, one for Python and one for the Typescript programming language.

## Needed infrastructure
DASF distributes messages via a central message broker. Currently we support a self-developed message broker called [dasf-broker-django](https://gitlab.hzdr.de/hcdc/django/dasf-broker-django), as well as an 'off-the-shelf' solution called [Apache Pulsar](https://pulsar.apache.org/). Both are quite versatile and highly configurable depending on your requirements. (also see: {ref}`messagebroker`)

### Apache Pulsar
In case you are just getting started, we recommend to use Apache Pulsar (see docker command below to start your local instance). It can be setup in various ways, e.g. locally, Docker or in a cluster. Please refer to the corresponding [documentation](https://pulsar.apache.org/docs/en/standalone) for your own setup. We tested DASF with Version 2.7.*, but in general all later versions should also be supported.

```{admonition} Docker Image
The Apache Pulsar Docker image can be found [here](https://hub.docker.com/r/apachepulsar/pulsar-standalone)

You can start a standalone instance of pulsar with:
`docker run -d --name pulsar -p 80:80 -p 8080:8080 -p 6650:6650 apachepulsar/pulsar-standalone:2.7.4`

You might also use our pulsar message broker [script](https://git.geomar.de/digital-earth/dasf/dasf-full-example/-/blob/main/pulsar-docker.sh) to start/stop a local pulsar-standalone docker image.
```

```{admonition} WebSocket Service
:class: warning

Since the DASF RPC messaging protocol uses Websockets, Pulsars Websocket-Service has to be enabled. In case you setup the standalone variant, this should already be the case.

On how to enable the WebSocket-Service for the other variants please consult the corresponding [documentation](https://pulsar.apache.org/docs/en/client-libraries-websocket/).
```

```{toctree}
---
caption: Table of Contents
maxdepth: 2
---
usage/quickstart.md
developers.md
api/index.md
```

## Open Source and Open Science

### License
All DASF modules are released under the `Apache-2.0` license.

### Repository
The individual DASF modules are developed via the following git group. Feel free to checkout the source code or leave comment via the service desk or directly via the issue tracker.

```{admonition} Gitlab Repository URL
:class: note

[https://git.geomar.de/digital-earth/dasf](https://git.geomar.de/digital-earth/dasf)
```

### Citation
In case you used DASF in your own work, please cite it using the following doi reference.

```{admonition} Citation DOI
:class: note

Eggert, Daniel; Dransch, Doris (2021): DASF: A data analytics software framework for
distributed environments. GFZ Data Services. [https://doi.org/10.5880/GFZ.1.4.2021.004](https://doi.org/10.5880/GFZ.1.4.2021.004)
```

### Acknowledgment
DASF is developed at the GFZ German Research Centre for Geosciences ([https://www.gfz-potsdam.de](https://www.gfz-potsdam.de)) and was funded by the Initiative and Networking Fund of the Helmholtz Association through the Digital Earth project ([https://www.digitalearth-hgf.de/](https://www.digitalearth-hgf.de/)).
