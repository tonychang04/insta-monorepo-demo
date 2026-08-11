import http.server, os, socketserver
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200); self.send_header("Content-Type","text/html"); self.end_headers()
        self.wfile.write(b"<h1>api service - Python, no Dockerfile, via nixpacks</h1>")
socketserver.TCPServer(("", int(os.environ.get("PORT", 8000))), H).serve_forever()
