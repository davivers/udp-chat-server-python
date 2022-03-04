import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server =  ('127.0.0.1', 4441)

while True:
    message = input()
    sock.sendto(bytes(message, 'ascii'), server)
    
