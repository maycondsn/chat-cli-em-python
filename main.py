import socket
from _thread import *
import time

# Definindo o servidor e a porta
HOST = '127.0.0.1'  # localhost
PORT = 33333

# Iniciando um objeto socket
client = socket.socket()


# aguardar mensagem do servidor
def listen_for_message_from_server(client):
    while True:
        message = client.recv(2048).decode('utf-8')
        print(message)


# enviar mensagens ao servidor
def send_messages_to_server(client):
    time.sleep(2)
    username = input('enter your username: ')
    while True:
        message = input('\nmessage: ')

        if (message == ''):
            print('empty message')
            exit(0)

        else:
            response = f'{username}: {message}'
            client.sendall(response.encode())


def communicate_to_server(client):
    # dividir o processo
    start_new_thread(listen_for_message_from_server, (client, ))
    send_messages_to_server(client)


# Tentando se connectar ao servidor
try:
    client.connect((HOST, PORT))
except socket.error as e:
    print(str(e))

print(f'client online in {HOST}:{PORT}')

communicate_to_server(client)
