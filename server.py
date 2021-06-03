from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

while True:
  serverSocket.listen()
  print("[SERVER] The server is wait for connection..")
  connection, clientAddress = serverSocket.accept()
  print('[SERVER] Got connection from ', clientAddress)
  
  connected = True
  
  while connected:
    message_length = connection.recv(2048).decode()
    message_length = int(message_length)
    message = connection.recv(message_length).decode()
    if (message == 'DC'):
      connected = False
      
    ##sendback
    connection.send(('Masuk '+ message + '\n').encode())
    
  if(connected == False):
    print('[SERVER] Connection from '+str(clientAddress[0])+ ':'+ str(clientAddress[1])+ ' is disconnected\n')
    
  connection.close()
