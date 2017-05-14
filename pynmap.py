import nmap
import os
import sys
import requests
ip = sys.argv[1]
username = "admin"
password = "password"
#artifactory creds

createdir = "http://127.0.0.1:8081/artifactory/phish/"+ip+"/"
r = requests.put(createdir, auth=(username,password))
#Makes sure directory is created before uploading
nm = nmap.PortScanner()
nm.scan(hosts=ip,arguments='-T4 -A -v')
print(nm.csv())
csvfile = nm.csv()
f = open('scan.csv','w')
f.write(csvfile)
f.close()
#Saves results in CSV format. Need to convert to JSON in the future
url = "http://127.0.0.1:8081/artifactory/phish/"+ip+"/scan.csv"
response = requests.put(url, data = open('scan.csv','rb'),auth=(username,password))
