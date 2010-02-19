#!/usr/bin/python3

import socket
from http.server import SimpleHTTPRequestHandler, HTTPServer

def main():
    try:
        server = None
        for port in range(8080, 8180):
            try:
                server = HTTPServer(('', port), SimpleHTTPRequestHandler)
            except socket.error:
                continue
            print('Listening on port {0}'.format(port))
            break

        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()

if __name__ == '__main__':
    main()
