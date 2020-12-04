# Event_B: Connect to listening server.
import socket
sock = socket.socket()
host = input(str("Enter server adress: "))
port = 81
sock.connect((host,port))
print("Connection Acheived! Huzzah!")

# Event_D: Now receive the transmitted file from event_B in server.py
print("Enter file name to receive: ")
fileName = input()
file = open(fileName, 'wb')             # open in "write bytes mode"
text = sock.recv(1024)                  # read info in file (may change!)
file.write(text)                        # write to the data
file.close()                            # close the file
print("File received!")                 # congragulatory message!
