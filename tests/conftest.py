import pytest
from pipeline.api_calls import Requests


@pytest.fixture(scope="session")
def sensor_interval():
    return "sensor_interval:get:system/1"


@pytest.fixture(scope="session")
def post_ph():
    return "ph:post :0.0"


@pytest.fixture(scope="session")
def post_ph_pump():
    return "task: post: 0: ph"


@pytest.fixture(scope="session")
def req():
    return Requests()


@pytest.fixture(scope="session")
def parsed_sense_interval():
    return {
        "data": "system/1",
        "request": "get",
        "type": "sensor_interval"
    }


@pytest.fixture(scope="session")
def parsed_ph_high():
    return {
        "data": "system/1",
        "request": "get",
        "type": "ph_high"
    }


@pytest.fixture(scope="session")
def parsed_post_ec():
    return {
        "data": "0",
        "request": "post",
        "type": "ec"
    }


@pytest.fixture(scope="session")
def parsed_post_ec_task():
    return {
        "data": {"data": "0", "task_type": "ec"},
        "request": "post",
        "type": "task"
    }
