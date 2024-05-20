import socket

def send_code_snippet(code):
    socket_path = "/tmp/code_socket"
    
    code_to_send = f"# NEP-START\n{code}\n# NEP-END"
    
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client.connect(socket_path)
    client.sendall(code_to_send.encode())
    client.close()

if __name__ == "__main__":
    contents = []
    while True:
        try:
            line = input()
            contents.append(line)
        except EOFError:
            break
    send_code_snippet("\n".join(contents))

