import socket

host ="127.0.0.1"

client_socket = socket.socket(socket.AF_INET_socket.SOCK_STREAM)
client_socket.connect((host,port))

message = input(">> ")

while message.lower()strip()!="quit":
    
    
    client_socket.send(message.encode())
    
    data= client_socket.recv(1024).decode()
    
    print("Su meşaj geldi :"+str(data))
    
    message = input(">> ")
    
    client_socket.close()
    
    
    
    
    

 