
from http.server import HTTPServer, BaseHTTPRequestHandler


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # Now, write the response body.
        self.wfile.write("Olá Mundo HTTP!".encode())

if __name__ == '__main__':
    server_address = ('', 7001)  # Serve on all addresses, port 7001.
    httpd = HTTPServer(server_address, MyHandler)
    print("Server rodando na porta: "+str(7001))
    httpd.serve_forever()
    
