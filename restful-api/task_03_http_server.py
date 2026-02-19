#!/usr/bin/python3
"""Basic HTTP server with multiple endpoints."""

import http.server
import socketserver
import json


class MyHandler(http.server.BaseHTTPRequestHandler):
    """Custom request handler."""

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            # Root endpoint
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            # JSON data endpoint
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            # Status endpoint
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            # Undefined endpoint → 404
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found: The requested endpoint does not exist.")


if __name__ == "__main__":
    PORT = 8000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Serving on port {PORT}...")
        httpd.serve_forever()
