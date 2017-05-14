## To Do:

### Create module jobs

- Subdomain parser 'subdomains'
- Nmap scanner 'nmap'
- Nikto scanner 'nikto'
- Dirbuster scanner 'dirbuster'
- Create script to generate all Jenkins jobs
java -jar jenkins-cli.jar -s http://127.0.0.1:8080/ get-job $jobname >>recon.xml
- Create script to generate initial Artifactory repositories and upload scripts

### Migrate from Artifactory Pro to OSS

- Use only as a file repository
- Deprecate use of properties API
- Save all information as JSON/CSV/XML file

### Webapp to view all of this data

- Recommend Flask or MEAN stack
- Will use OSS API calls to grab JSON information