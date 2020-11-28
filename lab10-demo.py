# Disclaimer
# This template is meant for educational purpose only.
# if you submit this chances are you will get
# an Academic offence...

import socket
import os

socket.setdefaulttimeout(1)

def pingScan(network, sHost, eHost):
  print('Scanning for hosts')
  finalResults = []
  for host in range(sHost, eHost + 1):
    scannedHost = str(network) + '.' + str(host)
    if os.system(r'ping -n 1 ' + scannedHost + '| find "TTL"') == 0:
      print(scannedHost, 'is Online!')
      finalResults.append(scannedHost)
  return finalResults

def hostPortScan(host, sPort, ePort):
  print('Scanning', host, 'for open ports')
  for port in range(sPort, ePort + 1):
    connection = socket.socket()
    result = connection.connect_ex((host, port))
    if result == 0:
      print('Port', port, 'Open!')
    connection.close()
  return

nw = '192.168.1'  # network to scan for online hosts
sh = 1  # start of host range
eh = 254  # end of host range
sp = 1  # begining of port range
ep = 65535  # end of port range
onlineHostsFound = pingScan(nw, sh, eh)
for host in onlineHostsFound:
  hostPortScan(host, sp, ep)

# start of FTP server code
# run this code on server machine
from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer
authorizer = DummyAuthorizer()
authorizer.add_user('PythonUsers', 'Info3128!', '.', perm='elradfmwMT')
handler = FTPHandler
handler.authorizer = authorizer
handler.banner = 'My FTP Server'
address = ("0.0.0.0", 2123)
server = servers.FTPServer(address, FTPHandler)
server.serve_forever()
# end of FTP server code

# start of FTP client Code
# run this code on client machine
from ftplib import FTP
ftpHost = '192.168.1.1'  # change this to ip of the machine running server
ftp = FTP()
ftp.connect(ftpHost, 2123)
ftp.login('PythonUsers', 'Info3128!')
ftp.close()
# end of client code.
