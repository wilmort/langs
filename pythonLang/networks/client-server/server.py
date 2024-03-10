import socket
import threading

HEADER = 64
# assign a port
PORT = 5050
# get server address
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
print("Host address: "+ SERVER + " Port: " + str(PORT))
FORMAT = 'utf-8'
DISCONN_MSG = "DISCONNECTED"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    
    print(f"[NEW CONNECTION] {addr} has connected.")
    connected = True
    
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length: 
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            
            if msg == DISCONN_MSG:
                connected= False            
            
            print(f"[{addr, msg}]")

            print("[THIS SERVER]: ", end='')
            reply = input()
            reply_msg = reply.encode(FORMAT)
            conn.send(reply_msg)

            if reply_msg.decode(FORMAT) == "close":
                conn.close()
                print("Connection closed by server.")

        
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {server}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target= handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]: {threading.active_count() - 1}")


print("[STARTING ] Server is starting...")
start()
