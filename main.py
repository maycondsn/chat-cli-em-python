import socket
from threading import Thread

def recv_message(): # thread para receber dados do servidor
    while True:
        print(sock.recv(1024).decode())

def setup():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.connect(('localhost', 3333))

    return sock

sock = setup()

sock.sendall(input('nickname: ').encode()) # envia o nickname para o servidor

Thread(target = recv_message, daemon = True).start() # inicializa a thread

while True: # loop para enviar mensagens
    sock.sendall(input().encode())
