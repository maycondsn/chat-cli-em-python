import socket

# Definindo o servidor e a porta
HOST = '127.0.0.1'  # localhost
PORT = 3333

# Iniciando um objeto socket
client = socket.socket()

# Tentando se connectar ao servidor
try:
    client.connect((HOST, PORT))
except socket.error as e:
    print(str(e))

print(f'client online in {HOST}:{PORT}')

# Loop para aguardar uma mensagem do servidor
while True:
    message = client.recv(2048).decode('utf-8')
    print(message)
