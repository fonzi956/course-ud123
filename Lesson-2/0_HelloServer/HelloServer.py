#!/usr/bin/env python3
#
# The *hello server* is an HTTP server that responds to a GET request by
# sending back a friendly greeting.  Run this program in your terminal and
# access the server at http://localhost:8000 in your browser.

from http.server import HTTPServer, BaseHTTPRequestHandler

#the from syntax of import so that I don't have to type http.server over and over in my code.


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):


#This is the handler class. It inherits from the BaseHTTPRequestHandler parent class,
#which is defined in http.server. I've defined one method, do_GET, which handles HTTP GET requests.
#When the web server receives a GET request, it will call this method to respond to it.


        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

#The next thing the server needs to do is send HTTP headers.
#The parent class supplies the send_header and end_headers methods for doing this.
#For now, I'm just having the server send a single header line — the Content-type header telling the client that the response
#body will be in UTF-8 plain text.


        # Now, write the response body.
        self.wfile.write("Hello, HTTP!\n".encode())

#The last part of the do_GET method writes the response body.

#The parent class gives us a variable called self.wfile, which is used to send the response.
#The name wfile stands for writeable file. Python, like many other programming languages,
#makes an analogy between network connections and open files: they're things you can read and write data to.
#Some file objects are read-only; some are write-only; and some are read/write.

#self.wfile represents the connection from the server to the client; and it is write-only; hence the name.
#Any binary data written to it with its write method gets sent to the client as part of the response. Here,
#I'm writing a friendly hello message.

#What's going on with .encode() though?

#An HTTP response could contain any kind of data, not only text.
#And so the self.wfile.write method in the handler class expects to be given a bytes object —
#a piece of arbitrary binary data — which it writes over the network in the HTTP response body.

#If you want to send a string over the HTTP connection, you have to encode the string into a bytes object.
#The encode method on strings translates the string into a bytes object, which is suitable for sending over the network.
#There is, similarly, a decode method for turning bytes objects into strings.

#That's all you need to know about text encodings in order to do this course.
#However, if you want to learn even more, read on ...


if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()

#This code will run when we run this module as a Python program, rather than importing it.
#The HTTPServer constructor needs to know what address and port to listen on;
#it takes these as a tuple that I'm calling server_address. I also give it the HelloHandler class,
#which it will use to handle each incoming client request.

#At the very end of the file, I call serve_forever on the HTTPServer, telling it to start handling HTTP requests.
#And that starts the web server running.
