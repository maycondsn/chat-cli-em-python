import socket
from _thread import *

# Definindo o servidor e a porta para a conexão
HOST = '127.0.0.1'
PORT = 33333

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


def thread_client(client):
    # envia uma mensagem ao cliente conectado
    client.send(str.encode(str(f'Connected!')))


# loop para aceitar as conexões
while True:
    client, addres = server.accept()
    print(f'Connected to {addres[0]}:{addres[1]}')
    start_new_thread(thread_client, (client, ))
