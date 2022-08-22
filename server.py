import socket
from _thread import *
from color import colored

# Definindo o servidor e a porta para a conexão
HOST = '127.0.0.1'
PORT = 30000
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


def send_message_to_all(sender, message):
    for user in clients:
        if (user[1] != sender):
            send_messages_to_client(user[1], message)


def list_clients_connected(client, username):
    for i in clients:
        if (username != i[0]):
            message = f'\nSERVER ~ {i[0]} is online!'
            send_messages_to_client(client, message)


def send_messages_to_client(client, message):
    client.sendall(message.encode())


def listen_messages(client, username):
    while True:
        data = client.recv(2048).decode('utf-8')
        message = f'[{username}]: {data}'
        send_message_to_all(client, message)


def thread_client(client):
    while True:
        try:
            username = colored(client.recv(2048).decode('utf-8'))
            clients.append((username, client))
            send_message_to_all(client, f'\n{username} online!')

            list_clients_connected(client, username)
            break
        except:
            print('username is empty')
            break

    start_new_thread(listen_messages, (client, username))


# loop para aceitar as conexões
while True:
    client, addres = server.accept()
    print(f'[+] [{addres[0]}]:[{addres[1]}]')
    start_new_thread(thread_client, (client, ))
