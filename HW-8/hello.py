from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def home():
    return render_template("Hello_world.html")


@app.route('/login/')
# @app.route('/login', methods=['GET', 'POST'])
@app.route('/login/<name>')
def login(username=None):
    return render_template("login.html", username=username)


@app.route('/about/')
@app.route('/about/<name>')
def about(username=None):
    return render_template("about.html", username=username)


# @app.route('/')
# def index():
#     if 'username' in session:
#         return 'Logged in as %s' % escape(session['username'])
#     return 'You are not logged in'






if __name__ == '__main__':
    app.run()
