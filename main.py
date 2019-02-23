from flask import Flask, render_template, request, session, flash
from graph import createPlotGraph
import sys
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Database Connection

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="hipas",
    password="sy42azyc",
    hostname="hipas.mysql.pythonanywhere-services.com",
    databasename="hipas$default",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', the_title='HIPAS')

if __name__ == '__main__':
    app.secret_key = 'thebiglebowski;'
    app.run(debug=True)

