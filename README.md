# OffSecCI
#### ** Work in Progress**

This repository has PoC scripts for what I call 'OffSecDevOps'. Combining pentesting tools, python and jenkins to automate the initial reconnaissance phase in a penetration scan.

#### Files:

#### Phishing:
- data.zip - Phishtank data, you need to unzip this
- pynmap.py - Should be run in a jenkins job and given an IP Address. Results will be saved in the file repository
- build.py - Uses mechanize to grab quick information about the URL
- startbuild.py - Starts jenkins jobs
- sites.txt - URL's for every reported Phishing URL
- crawl.py - Crawls through sites.txt, if directory indexing is found, looks for a .zip for, if .zip file is found, download the source


#### OffSecDevops:
- subdomainenum.py - takes two inputs: website name(e.g. 'att.com') and file containing list of subdomains. Will put IP Addresses and Subdomains, and send them to a Jenkins job for Nikto and Nmap scan
- subdomain - list of top 5000 subdomains


### To Do:
- Find/Create a Frontend service to view all of this information
- Docker Image?
- Scripts to generate Jenkins jobs from scratch