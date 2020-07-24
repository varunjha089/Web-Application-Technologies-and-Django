"""
    https://docs.python.org/3/library/socket.html
    https://docs.python.org/3/howto/sockets.html
    https://realpython.com/python-sockets/
    https://www.geeksforgeeks.org/socket-programming-python/
    https://pymotw.com/2/socket/tcp.html
    https://www.youtube.com/watch?v=T0rYSFPAR0A
    https://www.youtube.com/watch?v=3QiPPX-KeSc
"""
from socket import *


def create_server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    try:
        server_socket.bind(('localhost', 9000))
        server_socket.listen(5)
        while 1:
            (client_socket, address) = server_socket.accept()

            rd = client_socket.recv(5000).decode()
            piece = rd.split("\n")

            if len(piece) > 0:
                print(piece[0])

            data = 'HTTP/1.0 200 OK\r\n'
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello, World!</body></html>\r\n\r\n"
            client_socket.sendall(data.encode())
            client_socket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("\nShutting down....\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    server_socket.close()


print("Access http://localhost:9000")
create_server()
