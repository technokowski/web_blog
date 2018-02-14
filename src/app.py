from src.common.database import Database
from src.models.user import User

__author__ = "technokowski"

# To run this locally so other machines can view it on network,
# change to app.run(host='0.0.0.0') The default port is 5000

from flask import Flask, render_template, request, session

app = Flask(__name__) #__main__
app.secret_key = 'jose'
app.debug = True

@app.route('/') # www.mysite.com/api/
def hello_message():
    return render_template('login.html')

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None

    return render_template("profile.html", email=session['email'])

if __name__ == '__main__':
    app.run(port=4995)







