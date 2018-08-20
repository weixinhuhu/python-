import socket
def clinetfunc():

    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    text="How are you"

    data=text.encode()

    sock.sendto(data,("127.0.0.1",7852))

    data,addr=sock.recvfrom(200)

    text=data.decode()

    print(text)

if __name__=='__main__':

    clinetfunc()