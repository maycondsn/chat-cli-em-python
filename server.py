import socket
from _thread import *

# Definindo o servidor e a porta para a conexão
HOST = '127.0.0.1'
PORT = 3333

# Iniciando um objeto socket
server = socket.socket()

# Vincular o objeto ao endereço
try:
    server.bind((HOST, PORT))
except socket.error as e:
    print(str(e))

# Botar o servidor em modo de escuta, aguardando uma conexão
print(f'Server online in {HOST}:{PORT}')
server.listen()

# loop para aceitar as conexões
while True:
    client, addres = server.accept()
    print(f'Connected to {addres[0]}:{addres[1]}')

    # envia uma mensagem ao cliente conectado
    client.send(str.encode(str(f'Connected to server!')))
