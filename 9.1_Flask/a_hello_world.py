"""Exercício 9.1(a) — aplicação Hello World em Flask."""
from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello_world():
    return "Hello World! API Flask funcionando."

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
