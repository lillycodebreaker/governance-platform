"""Serve the browser-local governance walkthrough; no API or shared database."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

if __name__ == "__main__":
    root = Path(__file__).resolve().parent / "portal" / "dist"
    handler = partial(SimpleHTTPRequestHandler, directory=str(root))
    with ThreadingHTTPServer(("127.0.0.1", 8765), handler) as server:
        print("AI Governance Lab: http://127.0.0.1:8765/", flush=True)
        server.serve_forever()
