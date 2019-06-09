from app import app
from flask.templating import render_template

@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Lena'}
    posts = [
        {
            "author": {"username": "Christian"},
            "body": "I tested this cool blog!",
        },
        {
            "author": {"username": "Kira"},
            "body": "This blog is lame!",
        }
    ]
    return render_template("index.html", 
                           title="Home",
                           user=user,
                           posts=posts)

@app.route("/testing")
def testing():
    return "You reached the testing page!"