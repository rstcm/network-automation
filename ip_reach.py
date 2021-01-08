import sys
import subprocess

#To define reachibility of IP address
def ip_reach(iplist):
    for ip in iplist:
        ip = ip.rstrip('\n')

        ping_reply = subprocess.call('ping %s /n 2' %(ip), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
        if ping_reply == 0:
            print('\n *{} is reachable \n'.format(ip))

        else:
            print('\n Sorry, {} is not reachable :( Check connectivity and try again \n'.format(ip))
            sys.exit()

#print(ip_reach(['127.0.0.1', '192.168.0.104', '10.10.10.4']))