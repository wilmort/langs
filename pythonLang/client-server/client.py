import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONN_MSG = "DISCONNECTED"
SERVER = "192.168.1.72"
print("Connection  target address: "+ SERVER + " at Port: " + str(PORT))
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

print(f"You are now connnected to: {ADDR}")

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    reply = client.recv(2048).decode(FORMAT)
    print(f"[{SERVER, reply}]")

connected = True

while connected:
    print("You: ", end='')
    msgToSend = input()
    send(msgToSend)