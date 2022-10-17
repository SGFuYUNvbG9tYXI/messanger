import socket
from threading import Thread
def server():
    HOST = ""  
    PORT = 5000
    
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((HOST, PORT))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    while True:
                        text = conn.recv(1024)
                        print ("Text from client: ",text.decode("utf-8"))
        except:
            print("Client connection lost")
            continue

def client():
    HOST = input("Enter server IP address: \n") 
    PORT = 5000
    
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                print ("Enter text: \n")
                while True:
                    text= input()
                    s.sendall(text.encode("utf-8"))
        except:
            print ("Not found server, reconncet...")
            continue
        
tread1 = Thread(target=client)
tread2 = Thread(target=server)
    
tread1.start()
tread2.start()
