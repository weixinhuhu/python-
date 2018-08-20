import socket
import datetime

def serverfun():

    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    addr="127.0.0.1",7852

    s.bind(addr)

    data,addr=s.recvfrom(500)

    print(data)

    text=data.decode()
    
    print(text,addr)

    rsp="I am vitas"

    data=rsp.encode()

    s.sendto(data,addr)

if __name__=='__main__':
    print("Starting Server........")
    serverfun()
    print("Ending Server.....")









