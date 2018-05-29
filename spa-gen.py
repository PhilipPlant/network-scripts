#!/usr/bin/python
 
''' generate Nexus switchport assignment documentation '''
 
import paramiko
import warnings
import getpass
import sys
 
# init
username = 'admin'
password = getpass.getpass('Password: ')
switches = ['Switch-01',
            'Switch-02',
            'Switch-03',
            'Switch-04']
command  = 'show int desc | inc Eth'
 
# prepare ssh
ssh = paramiko.SSHClient()
warnings.simplefilter(action='ignore', category=FutureWarning)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
# for each switch
for target in switches:
  print ('## Switch '+target+'\n')
 
  # poll and block
  ssh.connect(target, username=username, password=password)
  stdin, stdout, stderr = ssh.exec_command(command)
  stdout.channel.recv_exit_status()
  output = stdout.readlines()
  ssh.close
 
  # output markdown
  sys.stdout.write ('| Port | Speed | Description |\n|:---|:---|:---|\n')
  for line in output:
    col = 0
    sys.stdout.write ('|')
    for element in line.split():
 
      # first column is redundant
      if col != 1:
 
        # fix output quirks
        if element == ('1000'):
          element = '1G'
        elif element == ('--'):
          element = '  '
        sys.stdout.write (element)
 
        # concatenate fourth column in case of spaces in descriptions
        if col < 3:
          sys.stdout.write ('|')
          col += 1
        else:
          sys.stdout.write (' ')
      else:
        col += 1
 
    # end column
    if col == 3:
      sys.stdout.write ('\b|')

    sys.stdout.write ('\n')
  sys.stdout.write ('\n')
