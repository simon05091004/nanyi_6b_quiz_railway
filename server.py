import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = int(os.environ.get("PORT", 8080))

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)

    def log_message(self, format, *args):
        print(f"[{self.date_time_string()}] {format % args}")

if __name__ == "__main__":
    print(f"✅ Server running on port {PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
