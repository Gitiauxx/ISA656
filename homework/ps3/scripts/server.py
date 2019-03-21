import socket
import ssl

HOST = ''
PORT = 12345
CERT = 'server.crt'
KEY = 'server.key'
MESSAGE = 'YourFirstName.txt'

def main():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
   s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   print("Socket successfully created")

   s.bind((HOST, PORT))  
   print ("socket binded to %s" %(PORT))   

   # put the socket into listening mode 
   s.listen(5)      
   print("socket is listening" )       

   # create context and load key and certificate
   context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER) 
   context.load_cert_chain(CERT, KEY)        
  
   # a forever loop until we interrupt it or  
   # an error occurs 
   while True: 
      conn =  None
      
      # Establish connection with client. 
      c, addr = s.accept()      
      print('Got connection from', addr)

      # wrap the ssl context around the connection
      try: 
         conn = context.wrap_socket(c, server_side=True)
      

         # send a message
         message = 'Thank you for connecting'
         with open(MESSAGE, 'rb') as f:
            conn.sendfile(f) 
      
      except ssl.SSLError as e:
         print(e)

      finally:
         if conn:
            conn.close()
      

      

if __name__ == "__main__":
   main()
  
   