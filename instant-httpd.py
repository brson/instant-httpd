#!/usr/bin/python3

import socket
import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer

def main():
    try:
        server = None

        port = 0

        if (len(sys.argv) == 2):
            port = int(sys.argv[1])
            server = HTTPServer(('', port), SimpleHTTPRequestHandler)
        else:
            for port in range(8080, 8180):
                try:
                    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
                except socket.error:
                    continue
                break

        print('Listening on port {0}'.format(port))

        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()

if __name__ == '__main__':
    main()
