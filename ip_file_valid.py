import os.path #library for working with pathes
import sys  #library for working with system like quiting running file

# Function to check if file inputted exists or not
def ip_file_valid():
    ip_file = input(r'\n Enter a name of ip contained file (e. g. D:\\python\\ip.txt): ' )
    if os.path.isfile(ip_file) == True:
        print('File {} exists'.format(ip_file))
    else:
        print('\n Incorrect path or filename. Please try again')
        sys.exit()

    ip = open(ip_file, 'r') #opening the file for reading only
    ip.seek(0) # to put cursor at the beginnig of the file
    ip_list = ip.readlines()  #to store list of ip addresses in ip_list variable
    ip.close()
    return ip_list
a = ip_file_valid()
[print(i) for i in a]

