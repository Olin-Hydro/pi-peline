import os


SERIAL_PORT = os.getenv('SERIAL_PORT', 'Missing SERIAL_PORT environment variable')
BAUDRATE = os.getenv('BAUDRATE', 'Missing BAUDRATE environment variable')
API_URL = os.getenv('API_URL', 'Missing API_URL environment variable')
