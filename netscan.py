import platform
import subprocess
import time

def bruh(ip):
    global args
    if platform.system()=='Windows':
        args= f"ping -n 1 {ip}"
    elif platform.system()=='Linux':
        args= f"ping -c 1 {ip}"
    process= subprocess.Popen(args,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output= process.stdout.read().decode()
    subs= output.split(" ")
    for sub in subs:
        if sub[:4] == 'time':
            return 0
        elif sub[:11] == 'Unreachable':
            return 1
        elif sub[:7] == 'service':
            return 2

ip=input(print("Enter your network private IP:"))
start=int(input(print("Enter your scanning start point:")))
end= int(input(print("Enter your desired end point:")))

global p
p=start

time_prev=time.time()
#exact=time.ctime(time)
print("Starting scan at :",time_prev)

if (start>=0 and end<256):
    if (start<=end):
        for i in range(start,end+1):
            part= ip.split(".")
            ip2= part[0]+ "." + part[1]+ "." + part[2]+ "." +str(p)
            if (bruh(ip2)==0):
                print(ip2 +": It is UP")
            elif (bruh(ip2)==1):
                print(ip2 +": It is DOWN")
            elif (bruh(ip2)==2):
                print("Wrong IP provided")
                exit(0)    
            p=p+1 

    else:
        print("Your starting point exceeds the ending point")

    time_now=time.time()
    diff=time_now-time_prev
    print("Scan Ended.")
    print("Time taken for scanning :",diff)

else:
    print("Your starting and ending range must be within 0-255")
