import socket
import threading
from datetime import datetime

HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

print("Server is running...")

def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break

            time = datetime.now().strftime("%H:%M")
            final_message = f"[{time}] {message.decode()}"

            print(final_message)
            broadcast(final_message.encode(), client)

        except:
            break

    clients.remove(client)
    client.close()
    broadcast("A user has disconnected.".encode())

while True:
    client, address = server.accept()
    print(f"Connected with {address}")

    clients.append(client)

    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()