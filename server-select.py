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
                    
                    
                    a = data.splitlines()
                    print(a)
                    f = open ('result.txt', 'w')

                    for line in a:
                        

                        def isPalindrome(stripped):
                            return stripped == stripped[::-1]

                        
                        ans = isPalindrome(line)
                    
                        if ans:
                            d = "yes"
                        else:
                            d = "no"
                        output = line + "-" + d
                        print(output)
                        
                        f.write(output + '\n')
                    
                    f.close()
                    z = open('result.txt', 'r')    
                    b = z.readlines()
                    [sock.send(data.encode()) for data in b]
                    [print(str(sock.getpeername()), data) for data in b]
                    
                    
                    
                else:
                    sock.close()
                    input_socket.remove(sock)

except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)