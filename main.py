from flask import Flask, render_template, request, session, flash
from graph import createGraphFromSqlList
import sys
from flask_sqlalchemy import SQLAlchemy

#Adds row from sql obj to python dict src: https://stackoverflow.com/questions/1024847/add-new-keys-to-a-dictionary
def row2dict(row):
	d = {}
	for column in row.__table__.columns:
		d[column.name] = str(getattr(row, column.name))
	return d

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
	company = db.Column(db.String(15))
	plan_name = db.Column(db.String(40), primary_key=True)
	adult = db.Column(db.Float)
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
	print ("##########################")
	if request.method == "POST":
		query_data = []
		attempted_plan = request.form.getlist('PlanName')
		for plan in attempted_plan:
			query = InsuranceData.query.filter_by(plan_name = plan).all()
			for row in range(0, len(query)):
				query_data.append(row2dict(query[row]))

		createGraphFromSqlList(query_data)
		print(query_data)
		print(attempted_plan)

	print("=========================")

	return render_template('index.html', the_title='HIPAS')

if __name__ == '__main__':
	app.secret_key = 'thebiglebowski;'
	app.run(debug=True)

