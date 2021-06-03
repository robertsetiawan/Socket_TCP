from socket import *
serverName = 'localHost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

def send(msg):
    message = msg.encode()
    message_length = len(message)
    send_length= str(message_length).encode()
    clientSocket.send(send_length)
    clientSocket.send(message)
    
n = int(input('banyaknya anggota kelompok: '));
for i in range(n):
    message = input('input Nama(spasi)NIM: ')
    
    send(message)

    # menerima pesan dari server
    modifiedMessage = clientSocket.recv(2048)
    print(modifiedMessage.decode())
    
send('DC') ## disconnect a connection
clientSocket.close()
