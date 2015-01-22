# Copyright 2015 Rooshil Patel
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import socket
import sys
from thread import *

HOST = ""
PORT = 8081

try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error as error_code:
    print("Failed to create socket!")
    print("Error code: " + str(error_code[0]) + 
          ". Error Message: " + error_code[1])
    sys.exit()

print("Socket created successfully!")

try:
    s.bind((HOST, PORT))
except socket.error as error_code:
    print("Bind attempt failed.")
    print("Error code: " + str(error_code[0]) + 
          ". Error Message: " + error_code[1])
    sys.exit()

print("Socket successfully bound!")

s.listen(5)
print("Socket now listening.")

def Client_Thread(conn):
    conn.send("Hello and welcome to the world of sockets!" + "\r\n")
    
    while True:
        data = conn.recv(4096)
        if not data:
            break
        data2 = str(data)
        if data2[0] == chr(27):
            break
        data2 = data2[:len(data2)-2]
        reply = data2 + " Rooshil" + "\r\n"
            
        conn.sendall(reply)
        
    conn.send("Thank you for visiting the world of sockets! Good bye!" + "\r\n")    
    conn.close()

while 1:
    conn, addr = s.accept()
    print("Connected with: " + addr[0] + ":" + str(addr[1]))
    
    start_new_thread(Client_Thread, (conn,))
    
s.close()