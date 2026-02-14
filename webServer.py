#Overview
#This code implements a simple web server that listens for incoming HTTP requests on a specified port (default is 13331). When a request is received, it attempts to serve a file requested by the client. If the file is found, it sends the file's content along with a success HTTP header. If the file is not found, it sends a 404 error message.



# import socket module, which allows the server to communicate over the network.
from socket import *
# In order to terminate the program, if needed
import sys



def webServer(port=13331): # web server listens for incoming HTTP requests on specified port = 13331
  serverSocket = socket(AF_INET, SOCK_STREAM) #socket object is created using AF_INET = IPV4 and SOCK_STREAM = TCP. This socket will be used to establish TCP connections.
  
  #Prepare a server socket that will accept connections from any IP address
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1) #The web server Listens for incoming connections

  #Fill in end

  while True:
    #Establish the connection
    
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Accept connections from the client
    #Fill in end
    
    try:
      message = connectionSocket.recv(1024).decode() #A client is sending you a message (HTTP request)
      #Fill in end 
      filename = message.split()[1] #The server extracts the filename from the HTTP request.  The request is split into parts, and the second part (index 1) is the filename.
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], 'rb')     #fill in start - open file in binary mode
      #fill in end

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
      #Fill in start 
      header = b"HTTP/1.1 200 OK\r\n" # Response header for a successful request
      #Content-Type is an example on how to send a header as bytes. There are more!
      outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"


      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
      response = header + outputdata + b"\r\n" #Combine headers
      #Fill in end
               
      for i in f: #for line in file
        response = response + i       #Fill in start - append your html file contents 
      #Fill in end 
        
      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!

      # Fill in start
      connectionSocket.sendall(response) #Send the complete response (header + file content) to the client, which ensures all data is sent in one go.

      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response error message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      header = b"HTTP/1.1 404 Not Found\r\n"  # Response header for a not found request
      outputdata = b"Content-Type: text/html; charset=UTF-8\r\n\r\n"  # Content-Type header
      response = header + outputdata + b"<html><body><h1>404 Not Found</h1></body></html>"  # 404 response body
      connectionSocket.sendall(response)  # Send the 404 response
      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close() #to free up resources
      #Fill in end

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331) #checks if the script is being run directly and stats the web server on port 13331.




