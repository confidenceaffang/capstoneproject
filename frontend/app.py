from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def helloWord():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("./auth/login.html")

@app.route("/signup")
def signup():
    return render_template("./auth/signup.html")

if __name__ == "__main__":
    app.run(debug=True)