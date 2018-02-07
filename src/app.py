__author__ = "technokowski"

# To run this locally so other machines can view it on network,
# change to app.run(host='0.0.0.0') The default port is 5000

from flask import Flask, render_template

app = Flask(__name__) #__main__

list = [1,2,3,4,5,'poop']


@app.route('/') # www.mysite.com/api/
def hello_world():
    return ("Hello, world!")
'''
def index():
    return render_template('base.html', pages=list)
'''


if __name__ == '__main__':
    app.run(port=5000)







