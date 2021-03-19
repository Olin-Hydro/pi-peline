# pi-peline

This is an tool to facilitate communicate between hydro-api and circadia. This code will run on a raspberry pi, and act as a portal to the world wide web for our arduino running circadia.

- PySerial is used to communicate over usb between the arduino and the pi
- Messages sent from circadia will be mapped/transformed into GET and POST requests, and sent to hydro-api
- The response from hydro-api will be sent back to circadia
