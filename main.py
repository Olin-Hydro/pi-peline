import serial

from pipeline import SERIAL_PORT, BAUDRATE, Requests, parse_line


def run():
    """
    Loop that transforms serial data to api requests
    """
    s = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)
    req = Requests()
    print("Starting loop")
    while True:
        if s.in_waiting > 0:
            data = read_data(s)
            if not data:
                print(f"Failed parsing data")
                continue
            res = send_request(data, req)
            handshake(res, s)


def read_data(s):
    print("Reading")
    line = s.read_until().decode("utf-8").rstrip("\n")
    print(line)
    return parse_line(line)


def send_request(data, req):
    print(f"Sending Request: {data}")
    return req.handle_request(data)


def handshake(res, s):
    if res.status_code == 200:
        print(f"Relaying Message: {res.text}")
        s.write(bytes(res.text, "utf-8"))
    else:
        print(f"Error sending api request: {res}")


if __name__ == "__main__":
    run()
