import pytest


def test_get_interval(req, parsed_sense_interval):
    res = req.handle_request(parsed_sense_interval)
    assert res == 120


def test_get_ph_high(req, parsed_ph_high):
    res = req.handle_request(parsed_ph_high)
    assert res == 7


def test_bad_parse(req):
    with pytest.raises(AssertionError):
        _ = req.handle_request({"request": "bad request type"})


def test_post_ec(req, parsed_post_ec):
    res = req.handle_request(parsed_post_ec)
    assert res.status_code == 200
    data = res.json()
    assert data["ec"] == 0.0
    assert isinstance(data["log_id"], int)
    assert isinstance(data["timestamp"], str)


def test_post_ec_task(req, parsed_post_ec_task):
    res = req.handle_request(parsed_post_ec_task)
    assert res.status_code == 200
    data = res.json()
    assert data["data"] == "0"
    assert data["task_type"] == "ec"
    assert isinstance(data["log_id"], int)
    assert isinstance(data["timestamp"], str)