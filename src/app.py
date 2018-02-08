__author__ = "technokowski"

# To run this locally so other machines can view it on network,
# change to app.run(host='0.0.0.0') The default port is 5000

from flask import Flask, render_template

app = Flask(__name__) #__main__
app.debug = True

@app.route('/') # www.mysite.com/api/
def hello_message():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(port=4995)







