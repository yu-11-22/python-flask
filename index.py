from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/YunHui", methods=["GET"])
def hello_world():
    return render_template("index.html")

if __name__ == "__main__he":
    app.run(host = "0.0.0.0", port = 8000, debug = True)