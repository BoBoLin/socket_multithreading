# encoding: utf-8
import socket, sys
import threading
from threading import Thread
from SocketServer import ThreadingMixIn

#Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print "now active threads : " + str(threading.enumerate() )
        print "[+] New server socket thread started for " + ip + " : " + str(port)

    def run(self):
        data = csock.recv(2048)
        print "Server received data : ", data
        if str(data) == "exit":
            global stop
            stop = True
        csock.send("server got it.")
        """
        for t in threads:
            print str(t)
        """
        print "-----------------------------------------------\n"
        print "Multithreaded Python server : waiting for connections from TCP clients..."

# Multithreaded Python server : TCP Server Socket Program Stub
host = [host ip]
port = [port]
BUFFER_SIZE = 20 # Usually 1024, but we need quick response

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    sys.stderr.write("[ERROR] %s\n" % msg[1])
    sys.exit(1)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse tcp
sock.bind((host, port))

threads = []
stop = False
print "Multithreaded Python server : waiting for connections from TCP clients..."

while not stop:
    try:
        sock.listen(5)
        sock.settimeout(0.2)
        (csock, (c_ip, c_port)) = sock.accept()  #啟動server準備讓client傳送訊息
        newthread = ClientThread(c_ip, c_port)
        newthread.start()  # This invokes the run() method in a separate thread of control.
        threads.append(newthread)
        #print str(len(threads)) + " (threads list length)"

        if len(threads) == 10 :
            threads[0].join()
            threads.pop(0)

    except socket.timeout:
        pass

for t in threads:
    t.join()

