# RW API microservice utility for Python+Flask applications

[![Build Status](https://travis-ci.com/resource-watch/rw-api-microservice-python.svg?branch=main)](https://travis-ci.com/resource-watch/rw-api-microservice-python)
[![Test Coverage](https://api.codeclimate.com/v1/badges/fe857a0082ab7d0bbd64/test_coverage)](https://codeclimate.com/github/resource-watch/rw-api-microservice-python/test_coverage)

Library to register and integrate microservices in the [RW API](https://api.resourcewatch.org/).


## Requirements

This library is tested to work with following Python versions:
- 3.6+
- 2.7 (legacy)

Additionally, it requires the following Python libraries: 
- Flask (tested with v1.1.1)
- Requests

## Install

```shell
pip install RWAPIMicroservicePython
```

## Testing

```shell
tox
```

These tests run on multiple python versions in parallel. You may want/need to use something like `pyenv` to support the underlying version handling. If you are using `pyenv virtualenv` be sure to deactivate any envs before calling `tox`.

## Use in microservice

To bootstrap your microservice, use:

```python
import os
import json
import RWAPIMicroservicePython
from flask import Flask

app = Flask(__name__)

with open('register.json') as register_file:
    info = json.load(register_file)
with open('swagger.json') as swagger_file:
    swagger = json.load(swagger_file)

RWAPIMicroservicePython.register(
    app=app,
    gateway_url='https://control-tower.your.domain',
    token='microserviceTokenForControlTower',
)
```

To make a request to another microservice, use:

```python
from RWAPIMicroservicePython import request_to_microservice

def execute():
    config = {
        'uri': '/v1/dataset/1234',
        'method': 'POST',
        'body': {'key': 'value'}
    }
    response = request_to_microservice(config)
    if not response or response.get('errors'):
        raise DatasetNotFoundError(message='Dataset not found')

    dataset = response.get('data', None).get('attributes', None)
    return dataset
```

## Configuration

These are the values you'll need to provide when using this library:

- app: the [Flask](https://flask.palletsprojects.com) `app`.
- gateway_url: the URL of the API as a whole, where all other services will be reachable.
- token: JWT token to use on calls to other services.

