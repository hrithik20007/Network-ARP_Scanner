import platform
import subprocess

def bruh(ip):
    global args
    if platform.system=='Windows':
        args=f"ping -n 1 {ip}"
    elif platform.system=='Linux':
        args=f"ping -c 1 {ip}"
    process= subprocess.run(args,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print(stdout)

ip=input(print("Enter IP"))

bruh(ip)
