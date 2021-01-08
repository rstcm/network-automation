import paramiko
import os.path
import sys
import re
import time

#To define whether username\password file exists or not
user_file = input(r"Enter full path and name of user file (e. g. C:\Desktop\file.txt): ")
if os.path.isfile(user_file) == True:
    print('\n Username\password file exists \n')
else:
    print('\n Sorry, {} does not exists. Please, check and try again'.format(ip_file))
    sys.exit()
    
#To define whether command file exists or not
cmd_file = input(r"Enter full path and name of command file (e. g. C:\Desktop\file.txt): ")
if os.path.isfile(cmd_file) == True:
    print('\n Command file exists \n')
else:
    print('\n Sorry, {} does not exists. Please, check and try again'.format(ip_file))
    sys.exit()

def ssh_connection(ip):
    global user_file
    global cmd_file
    
    try:
        selected_user_file = open(user_file, 'r')
        selected_user_file.seek(0)
        
        username = selected_user_file.readlines()[0].split(',')[0].rstrip('\n')
        
        selected_user_file.seek(0)
        
        password = selected_user_file.readlines()[0].split(',')[1].rstrip('\n')
        
        session = paramiko.SSHClient()
        
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        
        session.connect(ip.rstrip('\n'), username = username, password = password)
        
        connection = session.invoke_shell()
        
        connection.send('enable\n')
        connection.send('terminal length 0\n')
        time.sleep(0)
        
        connection.send('\n')
        connection.send('configure terminal\n')
        time.sleep(0)
        
        selected_cmd_file = open(cmd_file, 'r')
        selected_cmd_file.seek(0)
        
        for command in selected_cmd_file.readlines():
            connection.send(command + '\n')
            time.sleep(2)
            
        selected_user_file.close()
        selected_cmd_file.close()
        
        command_output = connection.recv(65535).decode()
        
        if re.search('% Invalid input', command_output):
            print('There was at least one IOS syntax error on devive {}'.format(ip))
        
        else:
            print('\nDone for device {}:'.format(ip))
            
            
        [print(i) for i in list(command_output.split('\r\n'))]
        file = open(r'/1_ssh/configuration.txt', 'a')
        for i in list(command_output.strip('\r\n')):
            file.writelines(i)
        file.writelines('\n\n_______________________________________________________________________________________________\n\n')
        file.close()
        session.close()
        
    except paramiko.AuthenticationException:
        print('* Invalid username or password \n Please check username/password file and device configuration.')
        print('* Closing program... Bye!')
        
        
        
        
        

 