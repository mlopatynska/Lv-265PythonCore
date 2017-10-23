from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def main ():
    return render_template("index.html")

@app.route("/about")
def about ():
    return render_template("about.html")

@app.route("/skills")
def skills ():
    skills = ["HTML", "CSS", "JavaScript", "Python", "JQuery"]
    return render_template("skills.html", skills = skills)

@app.route("/pygame")
def pygame ():
    return render_template("pygame.html")

if __name__  == "__main__":
    app.run(debug=True)