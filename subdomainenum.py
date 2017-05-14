from __future__ import print_function
import sys
import re
import socket
import colorama
import requests
from colorama import Fore, Back, Style
from jenkinsapi import jenkins


def noarguments():
    print('Usage: python script.py website.com subdomainlist.txt')
    sys.exit(0)

if len(sys.argv) != 3:
    noarguments()


site = sys.argv[1] #the website you want to enumerate
dnslist = sys.argv[2] #list of subdomains
ips = []
domains = []

with open(dnslist) as f:
    for line in f:
        try:
            subdomain = line.rstrip() + "." + site

            print Fore.GREEN + socket.gethostbyname(subdomain) + " - " + subdomain
            print(Style.RESET_ALL)
            ip = socket.gethostbyname(subdomain)
            if ip not in ips:
                ips.append(ip)
            else:
                print "duplicate IP"
            domains.append(subdomain)
        except Exception:
        	pass

print ips
print domains


for ipp in ips:
    J = jenkins.Jenkins("http://127.0.0.1:8080", username="admin", password="") #insert jenkins password
    J.poll()
    url = 'http://127.0.0.1:8080/job/nmapscan/buildWithParameters?ip='+ipp
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, headers=headers,auth=(jusername,jpassword))
    #Calls your Jenkins builds for port scanning
    #nmap -T4 -A -v $ip

for domain in domains:
    J = jenkins.Jenkins("http://127.0.0.1:8080", username="admin", password="") #insert jenkins password
    J.poll()
    url = 'http://127.0.0.1:8080/job/nmapscan/buildWithParameters?='+domain
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, headers=headers,auth=(jusername,jpassword))
    #Calls your Jenkins builds for nikto scan
    print "Subdomain: "+ domain
    #nikto -h  www.att.com
