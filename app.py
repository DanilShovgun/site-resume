from flask import Flask, render_template
from data import resume_data

app = Flask(__name__)


@app.route("/")
def index():
    """
    Главная страница сайта (резюме).
    """
    return render_template("index.html", data=resume_data)

if __name__ == "__main__":
    app.run(debug=True)
