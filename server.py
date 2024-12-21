import socket

host = "127.0.0.1"
port = 25565

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))

server.listen()
while True:
    client, address = server.accept() 
    data = client.recv(1024) 
    print(data.decode("etf-8"))