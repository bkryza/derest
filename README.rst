derest - declarative REST client for Python
###########################################

.. image: https://travis-ci.org/bkryza/derest
.. image: https://img.shields.io/badge/License-Apache%202.0-blue.svg

Declarative, decorator-based REST client for Python.

.. contents::

Overview
========

This library provides an easy to use declarative REST API client, where
definition of the API methods using decorators automatically gives a working
REST client with no additional code.

For example:

.. code-block:: python

    from derest import RestClient, GET

    class DogClient(RestClient):
        def __init__(self, endpoint, auth = None):
            super(DogClient, self).__init__(endpoint, auth)

        @GET('api/breed/{breed_name}/list')
        def list_subbreeds(self, breed_name):
            """List all sub-breeds"""

    client = DogClient('https://dog.ceo/dog-api')

    print(client.list_subbreeds('hound'))


Installation
============

Using pip:

.. code-block:: bash

    pip install derest

Usage
=====

Authentication methods
----------------------
Authentication can be specified for the client by providing a proper
authentication object in the constructor, any valid `requests.auth`
object will work.

For each client object authentication methods can be provided in 2 ways: 
 * `set_default_auth(auth)` - allows to provide default authentication method for all endpoints
 * `add_auth(name, auth)` - allows to specify additional authentication methods, which can be specified for selected operations using `@auth(name)` decorator


License
=======

Copyright 2018 Bartosz Kryza <bkryza@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
Apache 2.0
