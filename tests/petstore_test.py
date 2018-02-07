import os
import pytest
import time
import xml.etree.ElementTree as ET

from .petstore_client import PetstoreClient


@pytest.fixture
def client():
    time.sleep(3)
    petstore_port = os.environ["SWAGGERAPI/PETSTORE_8080_TCP"]
    return PetstoreClient("http://0.0.0.0:%s/v2" % (petstore_port),
                          ("admin", "password"))


def test_find_by_status(client):

    res = client.find_pet_by_status()
    assert res == []

    res = client.find_pet_by_status_xml()
    root = ET.fromstring(res)
    assert root.tag == 'pets'
