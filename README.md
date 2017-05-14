# OffSecCI
#### ** Work in Progress**

While this project is only being used to analyze phishing sites and hacked servers, it can definitely be modified for penetration testing, hence the name 'OffSecCI'. This is a crude attempt at OffSecDevOps.

#### Files:
- data.zip - Phishtank data, you need to unzip this
- pynmap.py - Should be run in a jenkins job and given an IP Address. Results will be saved in the file repository
- build.py - Uses mechanize to grab quick information about the URL
- startbuild.py - Starts jenkins jobs

### To Do:
- Convert CSV files to JSON on the fly
- Find/Create a Frontend service to view all of this information
- Docker Image?