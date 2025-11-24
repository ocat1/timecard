#!/usr/bin/env python3
import http.server
import socketserver
import os

os.chdir(os.path.dirname(__file__))

PORT = 5000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Server running on http://0.0.0.0:{PORT}")
    httpd.serve_forever()
