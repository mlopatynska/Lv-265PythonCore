from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Hello_world.html")

@app.route('/login/')
@app.route('/login/<username>')
def login(username=None):
    return render_template("login.html", username=username)

@app.route('/about/')
@app.route('/about/<name>')
def about(username=None):
    return render_template("about.html", username=username)

if __name__ == '__main__':
    app.run()
