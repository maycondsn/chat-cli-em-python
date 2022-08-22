import socket
from _thread import *

# Definindo o servidor e a porta para a conexão
HOST = '127.0.0.1'
PORT = 3333
clients = []

# Iniciando um objeto socket
server = socket.socket()

# Vincular o objeto ao endereço
try:
    server.bind((HOST, PORT))
except socket.error as e:
    print(str(e))

# Botar o servidor em modo de escuta, aguardando uma conexão
print(f'Server online in {PORT}')
server.listen()


def send_message_to_all(message):
    for i in clients:
        send_messages_to_client(i[1], message)


def list_clients_connected(client):
    for i in clients:
        message = f'{i[0]} is online!\n'
        send_messages_to_client(client, message)


def send_messages_to_client(client, message):
    print(message)
    client.sendall(message.encode())


def listen_messages(client, username):
    while True:
        data = client.recv(2048).decode('utf-8')
        message = f'[{username}]: {data}'
        send_message_to_all(message)


def thread_client(client):
    # envia uma mensagem ao cliente conectado
    client.send(str.encode(str(f'Connected!')))

    # receber mensagens do client
    while True:
        try:
            username = client.recv(2048).decode('utf-8')
            clients.append((username, client))
            send_message_to_all(f'{username} is online!')
            list_clients_connected(client)
            break
        except:
            print('username is empty')
            break

    start_new_thread(listen_messages, (client, username))


# loop para aceitar as conexões
while True:
    client, addres = server.accept()
    print(f'Connected to {addres[0]}:{addres[1]}')
    start_new_thread(thread_client, (client, ))
