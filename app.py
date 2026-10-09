import os
import socket

from flask import Flask, jsonify, request

app = Flask(__name__)


def multiply(a: float, b: float) -> float:
    """Умножение двух чисел."""
    return a * b


@app.route("/")
def index():
    return (
        "<h1>Flask app is running in Docker! 🐳</h1>"
        f"<p>Hostname: {socket.gethostname()}</p>"
        f"<p>Python: {os.sys.version.split()[0]}</p>"
        "<p>Try <a href='/health'>/health</a> or "
        "<a href='/multiply?a=3&b=4'>/multiply?a=3&b=4</a></p>"
    )


@app.route("/health")
def health():
    return jsonify(status="ok", hostname=socket.gethostname())


@app.route("/multiply")
def multiply_route():
    try:
        a = float(request.args.get("a", ""))
        b = float(request.args.get("b", ""))
    except (TypeError, ValueError):
        return jsonify(error="Параметры a и b должны быть числами"), 400

    return jsonify(a=a, b=b, result=multiply(a, b))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
