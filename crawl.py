import mechanize
import requests
import sys
from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import re
import hashlib
import urllib
fname = "sites.txt"



def downloadsource(url):
    m = hashlib.md5()
    m.update(url)
    filename = m.hexdigest()
    urllib.urlretrieve(url,filename+".zip")
    #We're going to save the name of the ZIP file as the MD5 of the string


def findsource(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content)
    for link in soup.findAll('a'):
        if '.zip' in link.get('href'):
            downloadsource(url+"/"+link.get('href'))

def checkindex(url):
    try:
        br = mechanize.Browser()
        br.addheaders = [('User-agent', 'Firefox')]
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_robots(False)
        br.set_handle_refresh(True, max_time=1)
        br.open(url)
        if 'Index of' in br.title():
            findsource(url)
    except:
        pass

def breakurl(url):
    regex = '(https?:\/\/)(.*)'
    match = re.search(regex,url)
    protocol = match.group(1)
    urls = match.group(2)
    urlbits = urls.split('/')
    for i in range(1,len(urlbits)):
        checkindex(match.group(1)+'/'.join(urlbits[:i]))

with open(fname) as f:
    for line in f:
        breakurl(line)