from pipeline.utils import parse_line


def test_full_post_ph(req, post_ph):
    data = parse_line(post_ph)
    res = req.handle_request(data)
    assert res.status_code == 200
    res_data = res.json()
    assert res_data["ph"] == 0.0
    assert isinstance(res_data["log_id"], int)
    assert isinstance(res_data["timestamp"], str)


def test_full_post_ph_task(req, post_ph_pump):
    data = parse_line(post_ph_pump)
    res = req.handle_request(data)
    assert res.status_code == 200
    res_data = res.json()
    assert res_data["data"] == "0"
    assert res_data["task_type"] == "ph"
    assert isinstance(res_data["log_id"], int)
    assert isinstance(res_data["timestamp"], str)
