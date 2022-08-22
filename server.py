import socket
from threading import Thread

class Server: # classe para gerenciar o servidor
    def __init__(self): # inicializa criando uma lista de clientes
        self.clients = []

    def recv_connection(self): # thread para receber conexoes e adicionar objetos de clientes na lista
        while True:
            client, client_addr = sock.accept()
            client = Client(client, client_addr)
            self.clients.append(client)
            Thread(target = client.recv_message).start() # inicialize a thread para receber dados do cliente

            print(f'[+] [{client_addr[0]}]:{[client_addr[1]]}')
            server.send_message(client, f'{client.nickname} connected'.encode())

    def send_message(self, sender, message): # enviar mensagem para todos os clientes exceto quem enviou a mensagem
        for client in self.clients:
            if client != sender:
                client.client.sendall(message)

class Client: # classe cliente para criar objetos de cliente
    def __init__(self, client, client_addr):
        self.client = client
        self.client_addr = client_addr
        self.nickname = client.recv(1024).decode()

    def recv_message(self): # thread para receber mensagens do cliente em questao e enviar para todos os outros
        while True:
            try:
                message = self.client.recv(1024)
                server.send_message(self, f'{self.nickname}: '.encode() + message)

            except:
                server.clients.remove(self)
                server.send_message(self, f'{self.nickname} disconnected'.encode())
                print(f'[-] [{self.client_addr[0]}]:{[self.client_addr[1]]}')
                break

server = Server() 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('localhost', 3333))
sock.listen(1)

Thread(target = server.recv_connection).start() # inicializa a thread para receber conexoes
