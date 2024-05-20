import socket
import os

def execute_code_snippet(code, global_context):
    try:
        exec(code, global_context)
    except Exception as e:
        print(f"Error: {e}")

def read_from_socket(conn):
    data = []
    while True:
        part = conn.recv(1024)
        if not part:
            break
        data.append(part.decode())
    return ''.join(data)

def main():
    socket_path = "/tmp/code_socket"
    
    if os.path.exists(socket_path):
        os.remove(socket_path)
    
    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server.bind(socket_path)
    server.listen(1)
    
    global_context = {}
    
    print("Listening for code snippets on Unix socket...")

    try:
        while True:
            conn, _ = server.accept()
            data = read_from_socket(conn)
            conn.close()
                            
            print("\t[x] Running..")
            execute_code_snippet(data, global_context)
            print("\t[x] Done")

            print()
    except KeyboardInterrupt:
        print("Shutting down.")
    finally:
        server.close()
        if os.path.exists(socket_path):
            os.remove(socket_path)

if __name__ == "__main__":
    main()
