import socket

#defining socket object
#AF_INET corresponds to ipv4 and SOCK_STREAM to TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting  client socket to the server
s.connect((socket.gethostname(), 3232))

#receiving msg from server
message = s.recv(1024)    #1024 is the buffer size, how large stream of data is being transferred
print(message.decode("utf-8"))
