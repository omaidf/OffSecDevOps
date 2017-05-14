from __future__ import print_function
import os
import sys
import json
import mechanize
import requests
import sys
from mechanize import Browser
import time
from jenkinsapi import jenkins
import requests
import json

record = {}
username = "admin"
password = "password"
#artifactory creds
jusername = "admin"
jpassword = "" #Insert your own API token here
#jenkins creds
def startbuild(site,target,country,ip):
    record = {
    'url':site,
    'target':target,
    'country':country,
    'ip':ip
    }
    uploadurl = "http://127.0.0.1:8081/artifactory/phish/"+ip+"/"
    propurl = "http://127.0.0.1:8081/artifactory/api/storage/phish/"+ip+"/?properties=target="+target+";country="+country+";ip="+ip+";url="+site
    r = requests.put(uploadurl, auth=(username,password))
    #Creates directory
    r = requests.put(propurl, auth=(username,password))
    #Adds properties to directories

    J = jenkins.Jenkins("http://127.0.0.1:8080", username="admin", password="f0ea63c9558c1feab9f2792bbfcf065d")
    J.poll()
    url = 'http://127.0.0.1:8080/job/Recon/buildWithParameters?ip='+ip"&url="+site
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, headers=headers,auth=(jusername,jpassword))
    #Calls your Jenkins builds for port scanning

with open('verified_online.json') as json_data:
    output = json.load(json_data)
    for site in output:
        url = site["url"]
        target = site["target"]
        country = site["details"][0]["country"]
        ip = site["details"][0]["ip_address"]
        startbuild(url,target,country,ip)
        time.sleep(5) #You will need this to prevent your CI servers from going crazy

