import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print("[NEW CONNECTION] %s connected" %addr)
    connected = True
    while connected:
        msg_length = conn.recv(HEADER)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg==DISCONNECT_MESSAGE:
            connected=False
        
        print("[%s] %s" %addr %msg)
    conn.close()



def start():
    server.listen(0)
    print("server is listening on %s" %SERVER)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("[ACTIVE CONNECTYIONS] %i" %threading.activeCount()-1)



print("starting server...")
start()