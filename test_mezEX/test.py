import requests
import sys
import pprint

url = 'https://xn--90adear.xn--p1ai/check/auto'
r = requests.get(url, params='XTA217230D0240693')
if r.status_code / 100 != 2:
    print('failed to execute request, status_code: {page.status_code}')
    sys.exit(-1)
print(r.text)