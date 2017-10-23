from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/about/skill')
def skills():
    return render_template("skills.html")


@app.route('/about/project')
def project():
    return render_template("project.html")


if __name__ == '__main__':
    app.run(debug=True)
