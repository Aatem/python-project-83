from flask import Flask, render_template


app = Flask(__name__)
#app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    text = 'text'
    return render_template(
        'index.html',
        text=text
    )
