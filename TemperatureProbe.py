#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Tim F. Rieck"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "stenosis"

import sys
import json
import threading
import time
import datetime
import Adafruit_DHT
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

# Instance variables
PORT_NUMBER = 8080
TEMPERATURE = 0
HUMIDITY = 0
RESULT = ''

class TemperatureProbe():
	global data_as_json

	# Permanently read out the temperatur with a 10 sec delay and store to variable / as thread
	def get_data():
		global HUMIDITY
		global TEMPERATURE
		while True:
			try:
				HUMIDITY, TEMPERATURE = Adafruit_DHT.read_retry(22, 4)
				data_as_json()
				time.sleep(2)
			except Exception, e:
				print e

	# Determine the temp measurement as a JSON object	
	def data_as_json():
		global RESULT
		class Measurement(object):
			pass
		measurement = Measurement()
		measurement.temperature = '%.1f'%(TEMPERATURE)
		measurement.humidity = '%.1f'%(HUMIDITY)
		measurement.time = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")
		RESULT = json.dumps(measurement.__dict__)
	
	# Starts a basic http server to return the measurement result
	def start_http_server():
		class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
			def do_GET(self):
				self.send_response(200)
				self.send_header('Content-type', 'application/json')
				self.end_headers()
				self.wfile.write(RESULT)
		httpd = HTTPServer(('0.0.0.0', PORT_NUMBER), SimpleHTTPRequestHandler)
		httpd.serve_forever()

	# Main method
	if __name__ == "__main__":
		
		# init the first result value for the http server
		data_as_json()
		
		# start the temp sensor probe
		t1 = threading.Thread(target=get_data)
		t1.start()
		
		# start the http server
		t2 = threading.Thread(target=start_http_server)
		t2.start()
		
		while True:
			time.sleep(10)
	main()
