'''
Created on 7 mar. 2017

@author: martintc
'''
import socket

target_host = '127.0.0.1' # "www.google.com"
target_port = 9998 #80

'''
Creamos un objeto socket.
AF_INET indica que usaremos ipv4
SOCK_STREAM indica que usaremos protocolo TCP
SOCK_DGRAM nos indicaría UDP
'''
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

'''
Asumimos por defecto que la conexión tendrá éxito
Habría que gestionar error si esto no es así
'''
client.connect((target_host, target_port))

# Asumimos que es el server el que espera un evento para actuar
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = client.recv(4096)

print(response)
