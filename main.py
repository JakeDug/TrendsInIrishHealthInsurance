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

#define InsuranceData table + data
class InsuranceData(db.Model):

	__tablename__ = "insuranceData"
	plan_name = db.Column(db.String(40), primary_key=True)
	adult = (db.Float)
	young_adult_age_25 = db.Column(db.Float)
	young_adult_age_24 = db.Column(db.Float)
	young_adult_age_23 = db.Column(db.Float)
	young_adult_age_22 = db.Column(db.Float)
	young_adult_age_21 = db.Column(db.Float)
	young_adult_age_20 = db.Column(db.Float)
	young_adult_age_19 = db.Column(db.Float)
	young_adult_age_18 = db.Column(db.Float)
	child_one = db.Column(db.Float)
	child_two = db.Column(db.Float)
	child_three = db.Column(db.Float)
	child_four = db.Column(db.Float)
	newborn = db.Column(db.Float)
	date = db.Column(db.DateTime, nullable=False, primary_key=True)




@app.route('/', methods=["GET", "POST"])
def index():
	return render_template('index.html', the_title='HIPAS', insuranceData = InsuranceData.query.all())

if __name__ == '__main__':
    app.secret_key = 'thebiglebowski;'
    app.run(debug=True)

