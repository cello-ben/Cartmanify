from flask import Flask, render_template, request
from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)

@app.route('/', methods = ['GET', 'POST'])
def main():
    if request.method == 'POST':
        text = request.form['text']

        cartman = str(text).lower().replace('fine', 'fahn').replace('here', 'myah').\
            replace('mom', 'maaaaaaaaaaaaaam').replace('serious', 'seriously').\
            replace('authority', 'authoritah').replace('kyle', 'keel')
        return render_template('index.html', cartman = cartman)

    return render_template('index.html')

