from pipeline.utils import parse_line


def test_get_interval(sensor_interval):
    data = parse_line(sensor_interval)
    assert data["type"] == "sensor_interval"
    assert data["request"] == "get"
    assert data["data"] == "system/1"


def test_post_ph(post_ph):
    data = parse_line(post_ph)
    assert data["type"] == "ph"
    assert data["request"] == "post"
    assert data["data"] == "0.0"


def test_post_ph_pump(post_ph_pump):
    data = parse_line(post_ph_pump)
    assert data["type"] == "task"
    assert data["request"] == "post"
    assert data["data"] == {"data": "0", "task_type": "ph"}
