import os
import sys
import json
import mechanize
import requests
import sys
from mechanize import Browser


url = sys.argv[1]
ip = sys.argv[2]
site_record = {}
username = "admin"
password = "password"
#artifactory creds

br = mechanize.Browser()
br.addheaders = [('User-agent', 'Firefox')]
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_robots(False)
try:
    br.open(url)
    title = br.title()
    headers = br.response().get_all_header_names(normalize=True)
    if 'Server' in headers:
        serv = br.response().__getitem__('Server')
    else:
        serv = "N-A"
    if 'X-Powered-By' in headers:
        xpow = br.response().__getitem__('X-Powered-By')
    else:
        xpow = "N-A"

    site_record = {
        'Server': serv,
        'X-Powered-By':xpow,
        'Title':title
    }

    f = open('scan.json','w')
    f.write(site_record)
    f.close()
    url = "http://127.0.0.1:8081/artifactory/phish/"+ip+"/scan.json"
    print url
    response = requests.put(url, data = open('scan.json','rb'))

    uploadurl = "http://127.0.0.1:8081/artifactory/api/storage/phish/"+ip+"/?properties=Server="+serv+";X-Powered-By="+xpow+";title="+title
    r = requests.put(uploadurl,auth=(username,password),files=files)
except:
    sys.exit(0)