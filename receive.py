from bluetooth import *
import pyttxs3

engine = pyttsx3.init()
port = 1
server_sock=BluetoothSocket( RFCOMM )
while 1:
    print("loop")
    server_sock.bind(("",port))
    server_sock.listen(1)
    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)
    data = client_sock.recv(1024)
    client_sock.close()
    if data:
        print("received [%s]" % data)
        engine.say(data)
        engine.runAndWait()
        break
    else:
        print("no data available")
server_sock.close()

