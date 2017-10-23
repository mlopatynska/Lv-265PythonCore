from flask import Flask, session, redirect, url_for, escape, request, render_template

app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("Hello_world.html")

# @app.route('/login/')
# @app.route('/login/<name>')
# def login(username=None):
#     return render_template("login.html", username=username)

@app.route('/')
def index():
    # if 'username' in session:
    #     return 'Logged in as %s' % escape(session['username'])
    return render_template("Hello_world.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return render_template("login.html")
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'aaa'

@app.route('/about/')
@app.route('/about/<name>')
def about(username=None):
    return render_template("about.html", username=username)


if __name__ == '__main__':
    app.run()
