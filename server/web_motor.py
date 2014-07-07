#!/usr/bin/python3
import sys
from time import sleep
import http.server
import urllib.parse
import pifacedigitalio

JSON_FORMAT = "{{'relay0': {relay0_value}, 'relay1': {relay1_value}, 'led7': {led7_value}}}"
DEFAULT_PORT = 8000
STATUS_GET_STRING = "status"

class WebMotor(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        relay0 = self.pifacedigital.leds[0]
        relay1 = self.pifacedigital.leds[1]
        led7   = self.pifacedigital.leds[7]

        qs = urllib.parse.urlparse(self.path).query
        query_components = urllib.parse.parse_qs(qs)

        if STATUS_GET_STRING in query_components:
            status_value = int(query_components[STATUS_GET_STRING][0])
            if status_value == 1:
                relay1.turn_off()
#                sleep(1)
                relay0.turn_on()
            elif status_value == 2:
                relay0.turn_off()
#                sleep(1)
                relay1.turn_on()
            elif status_value == 3:
                relay0.turn_off()
                relay1.turn_off()
            else:
                print("query value error")
        else:
            print("query error")

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(JSON_FORMAT.format(
            relay0_value = relay0.value,
            relay1_value = relay1.value,
            led7_value   = led7.value,
        ), 'UTF-8'))

if len(sys.argv) > 1:
    port = int(sys.argv[1])
else:
    port = DEFAULT_PORT

WebMotor.pifacedigital = pifacedigitalio.PiFaceDigital()
server_address = ('', port)
try:
    WebMotor.pifacedigital.leds[7].turn_on()
    httpd = http.server.HTTPServer(server_address, WebMotor)
    httpd.serve_forever()
except KeyboardInterrupt:
    print("finish")
    WebMotor.pifacedigital.output_port.value = 0
    WebMotor.pifacedigital.deinit_board()
    httpd.socket.close()
