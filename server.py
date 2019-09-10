import socket

#defining socket object
#AF_INET corresponds to ipv4 and SOCK_STREAM to TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binding socket to some port on serber(localhost here)
s.bind((socket.gethostname(), 3232))   #port can be any 4 digit number

#server can handle only one connections so we keep a queue of 5 in case of multiple requests to the server at same time 
s.listen(5);    
# And now we listen
while True:
	clientcosket, address = s.accept() 
	print(F"Connection from {address} is established!")
	#send information to client socket,logically it should be s.send(), but this is it!
	clientcosket.send(bytes("Welcome to the server", "utf-8")) 
