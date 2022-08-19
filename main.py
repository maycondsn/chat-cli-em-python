import socket

HOST = '127.0.0.1'  # localhost
PORT = 3333

client = socket.socket()

client.connect((HOST, PORT))

print(f'client online in {HOST}:{PORT}')
