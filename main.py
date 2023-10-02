from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/all_cafes")
def all_cafes():
    return render_template('all.html')

@app.route("/add_new")
def add_new():
    return render_template('add.html')



if __name__ == "__main__":
    app.run(debug=True)


