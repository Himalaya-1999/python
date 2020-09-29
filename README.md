This project Contains Web UI of Linux Server
Here you just need to provide the Linux Commands and its output will be displayed on the browser window 
Just Clone these files and change the ip address according to your Linux server
In your Linux Server :
yum install httpd -y   ----> To install apache webserver
systemctl start httpd  ----> To start the httpd services
cd /var/www/cgi-bin/   ----> place all the docker files here 
chmod +x web.py        ----> make this file executable
chmod +x docker.py     ----> make this file executable
getenforce             ----> Check the SELinux mode
setenforce 0           ----> put the SELinux mode to permissive
update the public ip of your server in html file
!!KUDOS  You've Successfully setup your WEB UI for your Linux Server.
