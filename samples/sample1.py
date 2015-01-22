import socket
import sys

#sample 1 begins
try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error as msg:
    print("Failed to create socket!")
    print("Error code: " + str(msg[0]) + 
          ". Error Message: " + msg[1])
    sys.exit()
    
print("Socket created successfully!")
#sample 1 ends
#sample 2 begins

HOST = "www.ualberta.ca"
PORT = 80

try:
    remote_ip = socket.gethostbyname(HOST)
except socket.gaierror:
    print("Host name could not be resolved.")
    sys.exit()

print("IP address of " + HOST + " is: " + remote_ip + ".")

s.connect((remote_ip, PORT))
print("Socket connected to " + HOST + " on ip: " + remote_ip + ".")
#sample 2 ends
#sample 3 begins

message = "GET / HTTP/1.1\r\n\r\n"
try:
    s.sendall(message.encode("UTF-8"))
except socket.error as msg:
    print("Send failed!")
    print("Error code: " + str(msg[0]) + 
          ". Error Message: " + msg[1])    
    sys.exit()
print("Message sent successfully.")

#sample 3 ends
#sample 4 begins

reply = s.recv(4096)
print(reply)
s.close()