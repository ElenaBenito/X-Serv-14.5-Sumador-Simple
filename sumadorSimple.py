#!/usr/bin/python3

import socket

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

cont = None
try:
	while True:
		print('Waiting for connections')
		(recvSocket, address) = mySocket.accept()
		print('HTTP request received:')
		received = recvSocket.recv(2048)
		aux = str(received).split()[1][1:]
		
		if aux == 'favicon.ico':
			print('Navegador pide favicon! ')

		else:
			num = int(aux)	#Suponemos que la entrada va a ser siempre un entero.
			
			if cont == None:
				cont = num
				resultado = "Introduzca otro numero"
				print (num)

			else:
				suma = num + cont
				resultado = "La suma de " + str(cont) + " + " + str(num) + " es " + str(suma)
				cont = None
				print (num)
			
			recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                       			  "<html><body><h1>Sumador simple:<br><br>" + "\n" + resultado + 
								  "</h1></body></html>" +
							  	  "\r\n", 'utf-8'))

			recvSocket.close()

except KeyboardInterrupt:
	print(" --Closing binded socket")

mySocket.close()
