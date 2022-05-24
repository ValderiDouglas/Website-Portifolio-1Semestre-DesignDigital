from flask import Flask,url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/portifolio")
def protifolio():
    return render_template("page2.html")

@app.route("/contato")
def contato():
    return render_template("page3.html")

if __name__ == "__main__":
    app.run(debug=True)