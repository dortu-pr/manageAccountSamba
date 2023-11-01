# echo-server.py
# modifico anche qua

from classi.send_receve_sock import *
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Attendo connessione")
    conn, addr = s.accept()
    sr = SRS(conn)
    r = "Il server risponde: " + sr.ricevi()
    sr.invia(r)
