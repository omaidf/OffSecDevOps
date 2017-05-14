import nmap
import os
import sys
import requests
ip = sys.argv[1]
username = "admin"
password = "password"
#artifactory creds

createdir = "http://127.0.0.1:8081/artifactory/nmap/"+ip+"/"
r = requests.put(createdir, auth=(username,password))
#Makes sure directory is created before uploading
nm = nmap.PortScanner()
nm.scan(hosts=ip,arguments='-T4 -A -v')
print(nm.analyse_nmap_xml_scan())
csvfile = (nm.analyse_nmap_xml_scan())


f = open('scan.json','w')
f.write(str(csvfile))
f.close()
url = "http://127.0.0.1:8081/artifactory/nmap/"+ip+"/scan.json"
response = requests.put(url, data = open('scan.json','rb'),auth=(username,password))
