from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route("/")
def hello():
    version = os.getenv("APP_VERSION", "v2")
    return f"Hello from Phanishanker Balle CI/CD! Host={socket.gethostname()} Version={version}\n"

@app.route("/health")
def health():
    return "OK\n", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
