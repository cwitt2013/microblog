from app import app

@app.route("/")
@app.route("/index")
def index():
    return "Hello World!"

@app.route("/testing")
def testing():
    return "You reached the testing page!"