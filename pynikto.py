import nmap
import os
import sys
import requests
site = sys.argv[1]
sitehtml = sys.argv[1] + ".html"
username = "admin"
password = "password"
#artifactory creds

createdir = "http://127.0.0.1:8081/artifactory/nikto/"+site+"/"
r = requests.put(createdir, auth=(username,password))
#Makes sure directory is created before uploading

url = "http://127.0.0.1:8081/artifactory/nikto/"+site+"/"+sitehtml
response = requests.put(url, data = open(sitehtml,'rb'),auth=(username,password))
