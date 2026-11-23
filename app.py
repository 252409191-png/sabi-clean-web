
from flask import Flask, render_template
from pathlib import Path

app = Flask(__name__, template_folder=str(Path(__file__).resolve().parent / "static" / "templates"))

@app.route("/")
def inicio():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


