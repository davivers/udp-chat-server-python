from importlib.util import decode_source
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ('127.0.0.1', 4441)
sock.bind(server)


while True:
    msg_rec, address = sock.recvfrom(1024)
    print ("something sent:",str(msg_rec), address)
   
