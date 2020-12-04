# Event_A: Initialize connection to client
import socket
sock = socket.socket()
host = socket.gethostname()
port = 81
sock.bind((host,port))
sock.listen(1)
print(host)
print("Listening for any clientele...")
connection, addr = sock.accept()
print(addr, "Connected!")

# Event_C: get file and open to "read bytes mode" ('rb')
print("Enter file name to transfer: ")
fileName = input()
file = open(fileName, 'rb')             # open in "read bytes mode"
text = file.read(1024)                  # read info in file (may change!)
connection.send(text)                   # sends data to client
print("File transferred... Hooray!")    # congragulatory message!
