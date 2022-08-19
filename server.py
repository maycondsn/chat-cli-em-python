import socket

HOST = '127.0.0.1'
PORT = 3333

server = socket.socket()

server.bind((HOST, PORT))

print(f'Server online in {HOST}:{PORT}')
server.listen()

while True:
    client, addres = server.accept()
    print(f'Connected to {addres}')
