from flask import Flask , render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'efb7977948fb9be76ebd6700800b3852'

@app.route('/')
def login():
    return render_template("login.html")


if __name__ =='__main__':
    app.run(debug=True)