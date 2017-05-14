sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install git vim python-pip wget curl software-properties-common oracle-java8-installer  apt-transport-https -y
sudo add-apt-repository "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"
echo "deb https://jfrog.bintray.com/artifactory-debs jessie main" | sudo tee -a /etc/apt/sources.list
echo deb http://ftp.uk.debian.org/debian/ jessie main non-free | sudo tee -a /etc/apt/sources.list
echo deb-src http://ftp.uk.debian.org/debian/ jessie main non-free | sudo tee -a /etc/apt/sources.list

curl https://bintray.com/user/downloadSubjectPublicKey?username=jfrog | sudo apt-key add -
sudo apt-get install jfrog-artifactory-oss
wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
sudo add-apt-repository "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update -y
sudo apt-get install jenkins nikto nmap -y
sudo service artifactory start
sudo service jenkins start
git clone https://github.com/sullo/nikto.git