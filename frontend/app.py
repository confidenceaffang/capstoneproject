from flask import Flask, render_template

app = Flask(__name__)

sample_jobs = [
    {"title": "Software Developer", "image": "software_developer.webp"},
    {"title": "Doctor", "image": "doctor.avif"},
    {"title": "Chef", "image": "chef.jpg"},
    {"title": "Teacher", "image": "teacher.jpg"},
    {"title": "Aerospace Engineer", "image": "aero.webp"},
    {"title": "Archeologist", "image": "arch.jpg"},
    {"title": "Astronomer", "image": "astro.jpg"},
    {"title": "Chemist", "image": "chem.jpg"},
    {"title": "zoologist", "image": "zoo.jpg"},
    {"title": "Writer", "image": "writer.jpg"}
]

@app.route("/")
def helloWord():
    return render_template("index.html", jobs= sample_jobs)

@app.route("/login")
def login():
    return render_template("./auth/login.html")

@app.route("/signup")
def signup():
    return render_template("./auth/signup.html")

if __name__ == "__main__":
    app.run(debug=True)