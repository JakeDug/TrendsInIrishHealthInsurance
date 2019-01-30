import mysql.connector
from graph import *

mydb = mysql.connector.connect(
	host="fdb25.freehostingeu.com",
	user="2947937_hipas",
	passwd="Password123",
	database="2947937_hipas"
)

mycursor = mydb.cursor()

file_data = extractFromCSV("VhiJan2018")

sql = "INSERT INTO insuranceData (plan_name, adult, young_adult_age_25, young_adult_age_24, young_adult_age_23, young_adult_age_22, young_adult_age_21, young_adult_age_20, young_adult_age_19, young_adult_age_18, child_one, child_two, child_three, child_four, newborn, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (file_data[0], file_data[1], file_data[2], file_data[3], file_data[4], file_data[5], file_data[6], file_data[7], file_data[8], file_data[9], file_data[10], file_data[11], file_data[12], file_data[13], file_data[14], file_data[15])
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
