
#!/usr/bin/python

from fabric.api import *

env.user = 'user'
env.hosts = ['mail01', 'web01', 'ns01', 'zabbix']

@parallel
def aptupd():
	sudo('apt-get update')
	
def copy_conf():
	put("/etc/apticron/apticron.conf", "/etc/apticron/", use_sudo=True)

@parallel
def uptime():
	f = open("logfile", "a")
	
	log = run("uptime")
	f.write(log + '\n')

	f.close

	
def shutdown():
		sudo("shutdown -h now")

