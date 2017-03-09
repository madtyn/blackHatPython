'''
Created on 7 mar. 2017

@author: martintc
'''
import socket

target_host = "127.0.01"
target_port = 80

'''
Creamos un objeto socket.
AF_INET indica que usaremos ipv4
SOCK_DGRAM indica que usaremos protocolo UDP
SOCK_STREAM nos indicaría TCP 
'''
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Asumimos que es el server el que espera un evento para actuar
client.sendto("AAABBBCCC", (target_host, target_port))

data, addr = client.recvfrom(4096)

print(data)
