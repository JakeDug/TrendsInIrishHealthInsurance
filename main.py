from flask import Flask, render_template, request, session, flash
from graph import createGraphFromSqlList
from timeSeries import convertToDataFrame
import sys
from flask_sqlalchemy import SQLAlchemy
from linearRegression import linearReg
from svm import svm

#Adds row from sql obj to python dict src: https://stackoverflow.com/questions/1024847/add-new-keys-to-a-dictionary
def row2dict(row):
	d = {}
	for column in row.__table__.columns:
		d[column.name] = str(getattr(row, column.name))
	return d

app = Flask(__name__)
app.secret_key = "secretKey"



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
		error = ""
		attempted_plan_vhi = request.form.getlist('PlanName1')
		attempted_plan_ilh = request.form.getlist('PlanName2')
		attempted_plan_laya = request.form.getlist('PlanName3')
		attempted_startDate = request.form.get('startDate')
		attempted_endDate = request.form.get('endDate')

		for plan in attempted_plan_vhi:

			query = InsuranceData.query.filter_by(plan_name = plan).filter(InsuranceData.date.between(attempted_startDate, attempted_endDate)).all()

			for row in range(0, len(query)):
				query_data.append(row2dict(query[row]))

		for plan in attempted_plan_ilh:

			query = InsuranceData.query.filter_by(plan_name = plan).filter(InsuranceData.date.between(attempted_startDate, attempted_endDate)).all()

			for row in range(0, len(query)):
				query_data.append(row2dict(query[row]))

		for plan in attempted_plan_laya:

			query = InsuranceData.query.filter_by(plan_name = plan).filter(InsuranceData.date.between(attempted_startDate, attempted_endDate)).all()

			for row in range(0, len(query)):
				query_data.append(row2dict(query[row]))


		if len(query_data) > 0:
			#print(">>>>>>>>>>>>>>>>>")
			#print(convertToDataFrame(query_data))
			createGraphFromSqlList(query_data)

		else:
			flash("Error - Query returned no results for the plan(s) date combination")


	print("=========================")

	return render_template('index.html', the_title='HIPAS')

@app.route('/predict', methods=["GET", "POST"])
def predict():
	if request.method == "POST":
		query_data = []
		attempted_age = request.form.get('age')
		attempted_plan = request.form.get('PlanName')
		attempted_date = request.form.get('predDate')

		query = query = InsuranceData.query.filter_by(plan_name = attempted_plan).all()

		for row in range(0, len(query)):
			query_data.append(row2dict(query[row]))

		if len(query_data) > 0:
			flash(round(linearReg(query_data, attempted_age, attempted_date), 2))
			svm(query_data, attempted_age, attempted_date)

	return render_template('predict.html', the_title='HIPAS')

if __name__ == '__main__':
	app.secret_key = 'secretKey'
	app.run(debug=True)

