import sys

def ip_addr_valid(iplist):
    for ip in iplist:
        ip = ip.rstrip('\n')
        ip_octets = ip.split('.') # ip_octets >>>> octet list

        if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) !=169 or int(ip_octets[1]) != 254) and (0 <= int(ol[1]) <= 255 and 0 <= int(ol[2]) <= 255 and 0 <= int(ol[3]) <= 255):
            continue
        else:
            print('\n There was an invalid ip address in the file {}\n'.format(ip))
            sys.exit()
#a = ip_addr_valid(['192.168.10.100', '0.10.100.100'])
#print(a)
# (len(ol) == 4) >>>>> ip must contain for octets
# (1 <= int(ol[0]) <= 223) >>>>> first octet must be in this range to be usable
# (int(ol[0]) != 127)  >>>>> it should not be loopback ip address
#(int(ol[0]) !=169 or int(ol[1]) != 254) >>>>> It should not be so=called DHCP default address
# meaning there should not be address like this : 169.254. ... ok?
# (0 <= int(ol[1]) <= 255 and 0 <= int(ol[2]) <= 255 and 0 <= int(ol[3]) <= 255) last three octets should be in this range, too
