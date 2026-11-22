from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

ROUTES = {
    "/": "/templates/index.html",
    "/index": "/templates/index.html",
    "/login": "/templates/login.html",
    "/signup": "/templates/signup.html",
    "/menu": "/templates/menu.html",
    "/cart": "/templates/cart.html",
    "/dashboard": "/templates/dashboard.html",
}


class CafeHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(FRONTEND_DIR), **kwargs)

    def do_GET(self):
        path = urlparse(self.path).path
        if path in ROUTES:
            # redirect so the browser URL is /templates/..., making relative links work
            self.send_response(302)
            self.send_header("Location", ROUTES[path])
            self.end_headers()
            return
        super().do_GET()


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), CafeHandler)
    print("CafShap server is running!")
    print("Website: http://localhost:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped.")
        server.server_close()
