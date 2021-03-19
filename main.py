import serial
import time

from config import SERIAL_PORT, BAUDRATE

if __name__ == "__main__":
    s = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)
    s.flush()
    while True:
        if s.in_waiting > 0:
            line = s.readline().decode('utf-8').rstrip()
            print(line)
            s.write(b"success\n")
            
