import socket
import ssl

HOST, PORT = '127.0.0.1', 12345
CA = 'ca.pem'


def handle(conn):
    print(conn.recv().decode())

def main():
    sock = socket.socket(socket.AF_INET)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations(CA)
   
    c = context.wrap_socket(sock, server_hostname=HOST)
    try:
        c.connect((HOST, PORT))
        handle(c)
    finally:
        c.close()
    
if __name__ == "__main__":
    main()
