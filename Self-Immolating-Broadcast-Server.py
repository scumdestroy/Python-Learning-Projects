import socket
import sys
import argparse
import time
import os

# Help menu and arguments
parser = argparse.ArgumentParser( 
    description = '''Incendiary Countdown Suicide Server.  
    Broadcast a message across a finely tuned port for a set period of time.   ''', 
    epilog = """True champions have no time to look back and see fate pathetically chase their footprints. """) 
parser.add_argument('-ttl', type=int, default=666, help='Time to live')
parser.add_argument('-p', type=int, default=40004, help='port number')  
parser.add_argument('-msg', type=str, default="Stand behind your choices or lick the heels of fate eternal", help='Your call to those willing to connect') 
args=parser.parse_args() 

#Sock into a socket's sockets on the sock's socket stream
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Basic unimpressive but effective server settings
srv_ip = "127.0.0.1"
srv_port = args.p
buffersize = 1024

#Server's docking bay is go
s.bind((srv_ip, srv_port))
s.listen(1)
print("Server ready for an individual connection at port " + str(srv_port))

#Countdown until self-eradication commencing.
try:
	conn, addr = s.accept()
	print (addr, "Now Connected")
	recv(1024)
	time.sleep(args.ttl)
finally:
	print("My time has come to return to the void.")
	s.close()
	sys.exit()
