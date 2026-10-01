import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def inicio():
    return {"mensaje": "API de tareas funcionando"}


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(port=port, debug=True)