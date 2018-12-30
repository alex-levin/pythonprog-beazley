#!/usr/bin/env python3
# nextbus.py

from xml.etree.ElementTree import XML
import urllib.request
import sys

# ['nextbus.py', '22', '14787']
print('Command options:', sys.argv)
# This is how to make progrma quit
# raise SystemExit(0)

if len(sys.argv) != 3:
    # e.g., from video: nextbus.py 22 14787
    raise SystemExit('Usage: nextbus.py route stopid')

route = sys.argv[1]
stopid = sys.argv[2]


u = urllib.request.urlopen(
    'http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'.format(route, stopid))
data = u.read()
'''
b'<?xml version="1.0" encoding="UTF-8"?>
...
<pt>3 MIN</pt>
<pt>11 MIN</pt>
<pt>21 MIN</pt>
'''
# print(data)

doc = XML(data)

# import pdb; pdb.set_trace()    # Launch debugger

for pt in doc.findall('.//pt'):
    print(pt.text)

'''
Output:
3 MIN
16 MIN
24 MIN
'''
