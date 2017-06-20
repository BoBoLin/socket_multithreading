# Python TCP Client A
import socket 
 
host = [host ip]

port = [port]
BUFFER_SIZE = 2048
MESSAGE = "message A."
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))
 
tcpClientA.send(MESSAGE)     
data = tcpClientA.recv(BUFFER_SIZE)
print "Client2 received data:", data

tcpClientA.close()