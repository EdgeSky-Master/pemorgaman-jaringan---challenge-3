import socket
import select
import sys

server_address = ('127.0.0.1', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

input_socket = [server_socket]

try:
    while True:
        read_ready, write_ready, exception = select.select(input_socket, [], [])

        for sock in read_ready:
            if sock == server_socket:
                client_socket, client_address = server_socket.accept()
                input_socket.append(client_socket)

            else:
                data = sock.recv(1024).decode()
                
                if str(data):
                    
                    result = 0
                    operation_list = []

                    for letter in data:
                        operation_list.append(letter)
                    oprnd1 = operation_list[0]
                    operation = operation_list[1]
                    oprnd2 = operation_list[2]

                    num1 = int(oprnd1)
                    num2 = int(oprnd2)

                    if operation == "+":
                        result = num1 + num2
                    elif operation == "-":
                        result = num1 - num2
                    elif operation == "/":
                        result = num1 / num2
                    elif operation == "*":
                        result = num1 * num2
                    
                    
                    output = str(result)
                    client_msg = data + "=" + output + "\n"
                    print(str(sock.getpeername()), data + "=" + output)
                    sock.send(client_msg.encode())
                else:
                    sock.close()
                    input_socket.remove(sock)

except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)