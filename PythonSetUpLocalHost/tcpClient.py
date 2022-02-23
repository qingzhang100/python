import socket


def Main():
    host = '127.0.0.1'
    port = 65534

    s = socket.socket()
    s.connect((host, port))

    message = input("->")
    while message != 'q':
            s.send(message.encode())
            data = s.recv(1024)
            output = 'Received from server: '
            print(output + str(data))
            message = input("-> ")
    s.close()


if __name__ == '__main__':
        Main()
