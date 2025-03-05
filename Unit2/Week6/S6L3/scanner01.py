import socket
import random

IP = input("Inserisci l'indirizzo IP target: ")
porte = int(input("Inserisci la porta da scansionare: "))
num_pack = int(input("Quanti pacchetti vuoi inviare? "))

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    for i in range(num_pack):
        data = bytes([random.randint(0, 255) for i in range(1024)])
        sock.sendto(data, (IP, porte))
              
print(f"Sono stati inviati {num_pack} pacchetti di 1KB alla porta {porte} di {IP}.")