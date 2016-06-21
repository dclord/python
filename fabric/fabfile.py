
#!/usr/bin/python

from fabric.api import *

env.user = 'user'
env.hosts = ['mail01', 'web01', 'ns01', 'zabbix']


##################################################
##### Runs 'sudo apt-get update' on each     #####
##### env.hosts listed.                      #####
##################################################

@parallel
def aptupd():
	sudo('apt-get update')
	
##################################################
##### Copies apticron config from current    #####
##### server to all env.hosts                #####
##################################################

def copy_conf():
	put("/etc/apticron/apticron.conf", "/etc/apticron/", use_sudo=True)


##################################################
##### Runs uptime command then writes the    #####
##### output to the logfile.		     #####
##################################################

@parallel
def uptime():
	f = open("logfile", "a")
	
	log = run("uptime")
	f.write(log + '\n')

	f.close


##################################################
##### Shuts down the entire env.hosts	     #####
##### Beware using this function 	     #####
##################################################
	
def shutdown():
		sudo("shutdown -h now")

