import serial
import time

from pipeline import SERIAL_PORT, BAUDRATE, Requests, parse_line


def run():
    """
    Loop that transforms serial data to api requests
    """
    s = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)
    s.flush()
    while True:
        if s.in_waiting > 0:
            print("Reading")
            line = s.read_until(b"|||").decode("utf-8").rstrip("| ")
            print(line)
            data = parse_line(line)
            req = Requests()
            print("Sending Request")
            res = req.handle_request(data)
            if res not in ["404", "400"]:
                print("Relaying Message")
                s.write((res + "|||").encode('utf-8'))
            else:
                print("Error")
                pass # TODO: log error
            
            


if __name__ == "__main__":
    run()
