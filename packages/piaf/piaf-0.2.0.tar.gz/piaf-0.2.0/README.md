# Python Intelligent Agent Framework (piaf)

![pipeline status](https://gitlab.com/ornythorinque/piaf/badges/master/pipeline.svg)
![coverage report](https://gitlab.com/ornythorinque/piaf/badges/master/coverage.svg?job=test)
![PyPI - Downloads](https://img.shields.io/pypi/dm/piaf)
![PyPI - License](https://img.shields.io/pypi/l/piaf)
![PyPI](https://img.shields.io/pypi/v/piaf)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/piaf)

The aim of piaf is to provide a FIPA-compliant agent framework using Python. It uses **asyncio** to power agents.

## Project status

**The first official release is there!** After almost two years of development, I am now considering piaf is stable enough to start playing with it. I can't wait to see the amazing things you will do!

So, what is next? Well, there are still missing features in piaf and the next version will try to add some of them (I see you FIPA SL!).

## Features

Although piaf made some progress, it still needs some love to be fully compliant with the [FIPA specification](http://fipa.org/repository/standardspecs.html).

We provide some examples to help you understand what is possible to create with the current version, take a look at <https://gitlab.com/ornythorinque/piaf/-/tree/master/src/piaf/examples>.

### Supported features

- AMS (partial, only the query function)
- DF
- Communications within a platform
- Communications between two **piaf platforms** (with some limitations)

### Missing features

- FIPA SL support (only plain Python objects are supported)
- Federated DF
- Name resolution
- "Official" envelope representations (XML, bit-efficient) and MTPs (mainly HTTP, we don't plan to support IIOP)

## Documentation

The full documentation (both user and API) is available here: <https://ornythorinque.gitlab.io/piaf>
It will teach you how to install and run your agents.

## Author(s)

* ornythorinque (pierredubaillay@outlook.fr)
