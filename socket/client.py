import socket 

host ="127.0.0.1"

port=50001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host,port))

server_socket.listen()

conn,addr = server_socket.accept()
print("Connect from : "+str(addr))

while True:
    data= conn.recv(1024).decode()
    print(data)
    response_data="mesaj alındı"
    conn.send(response_data.encode())
    conn.close()
     