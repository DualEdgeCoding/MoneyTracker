from flask import *
import shelve as sh

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("Home.html")

if __name__ == '__main__':
    app.run()
