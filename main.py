from flask import Flask, render_template, request, session, flash
from graph import createPlotGraph
import sys

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', the_title='HIPAS')

if __name__ == '__main__':
    app.secret_key = 'thebiglebowski;'
    app.run(debug=True)

