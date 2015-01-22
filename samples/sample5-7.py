import socket
import sys

try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error as msg:
    print("Failed to create socket!")
    print("Error code: " + str(msg[0]) + 
          ". Error Message: " + msg[1])
    sys.exit()
    
print("Socket created successfully!")

#sample 5 begins
HOST = ""
PORT = 8888

try:
    s.bind(HOST, PORT)
except socket.error as msg:
    print("Bind failed! Error code: " + str(msg[0]) + 
          ". Error Message: " + msg[1])
    sys.exit()
    
print("Socket bind successful.")

s.listen(10)
print("socket is now listening.")
conn, addr = s.accept()

print("Connected with " + addr[0] + ":" + str(addr[1]))

try:
    remote_ip = socket.gethostbyname(HOST)
except socket.gaierror:
    print("Host name could not be resolved.")
    sys.exit()

print("IP address of " + HOST + " is: " + remote_ip + ".")

s.connect((remote_ip, PORT))
print("Socket connected to " + HOST + " on ip: " + remote_ip + ".")

message = "GET / HTTP/1.1\r\n\r\n"
try:
    s.sendall(message.encode("UTF-8"))
except socket.error as msg:
    print("Send failed!")
    print("Error code: " + str(msg[0]) + 
          ". Error Message: " + msg[1])    
    sys.exit()
print("Message sent successfully.")


reply = s.recv(4096)
print(reply)
s.close()