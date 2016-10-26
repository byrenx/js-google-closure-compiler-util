#!/usr/bin/python2.4

import httplib, urllib, sys

# Define the parameters for the POST request and encode them in
# a URL-safe format.

# dir = os.path.dirname(__file__)

# sample = os.path.join(dir, '/sample.js')

# print sample

import os
# js_files = []
js_codes = "";
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".js"):
             js_codes += open(os.path.join(root, file)).read()


params = urllib.urlencode([
	('js_code', js_codes),
    ('compilation_level', 'SIMPLE_OPTIMIZATIONS'),
    ('output_format', 'text'),
    ('output_info', 'compiled_code'),
  ])

# Always use the following value for the Content-type header.
headers = { "Content-type": "application/x-www-form-urlencoded" }
conn = httplib.HTTPConnection('closure-compiler.appspot.com')
conn.request('POST', '/compile', params, headers)
response = conn.getresponse()
data = response.read()

# TODO: write the output to a file e.g index.js
target_file = open(os.path.join(os.path.dirname(__file__), 'index.js'), 'w')
target_file.write(data);
print data
conn.close()
