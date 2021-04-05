import serial
import time

from pipeline import SERIAL_PORT, BAUDRATE
from pipeline import Requests

post_type = "post"
get_type = "get"


def run():
    """
    Loop that transforms serial data to api requests
    """
    s = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)
    s.flush()
    while True:
        if s.in_waiting > 0:
            line = s.readline().decode("utf-8").rstrip()
            if len(line) <= 0:
                continue
            data = parse_line(line)
            req = Requests()
            if data["request"] == post_type:
                res = req.post_data(
                    d_type=data["type"], data={data["type"]: data["data"]}
                )
            elif data["request"] == get_type:
                res = req.get_data(d_type=data["type"], args=data["data"])
            else:
                continue
            if res.status_code != 200:
                s.write(bytes(res.text + "error\n", 'utf-8'))
            else:
                s.write(bytes(res.text + "success\n", 'utf-8'))
                print("success")


def parse_line(line):
    """
    Incoming data format for logging sensor readings
    ph: post: 7.4
    ec: post: 600
    """
    data = {"data":""}
    data_list = line.split(":")
    data["type"] = data_list.pop(0).strip().lower()
    data["request"] = data_list.pop(0).strip().lower()
    for item in data_list:
        data["data"] += item.strip().lower()
    return data


if __name__ == "__main__":
    run()
