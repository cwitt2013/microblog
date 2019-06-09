from app import app
from flask.templating import render_template

@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Lena'}
    return render_template("index.html", 
                           title="Home",
                           user=user)

@app.route("/testing")
def testing():
    return "You reached the testing page!"