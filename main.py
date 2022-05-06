import schedule
import time
import smtplib
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

recipients = []
messages = {}
username = ""
password = ""

def readSqliteTable():
	try:
		sqliteConnection = sqlite3.connect('data.db')
		cursor = sqliteConnection.cursor()
		print("Connected to SQLite")

		sqlite_select_query_1 = """SELECT * from User""" 
		cursor.execute(sqlite_select_query_1)

		records = cursor.fetchall()
		for row in records: 
			recipients.append(row[2])

		sqlite_select_query_2 = """SELECT * from Newsletter"""
		cursor.execute(sqlite_select_query_2)

		result = cursor.fetchall()
		for row in result:
			messages[row[1]] = row[2]
			
		cursor.close()
		
	except sqlite3.Error as error:
		print("Failed to read data from sqlite table", error)
	
	finally:
		if sqliteConnection:
			sqliteConnection.close()
			print("The SQLite connection is closed")

readSqliteTable()

def message(subject="", text=""):
	msg = MIMEMultipart()
	msg['Subject'] = subject  
	msg.attach(MIMEText(text))
	return msg

def mail(title):
	smtp = smtplib.SMTP('smtp.gmail.com', 587)
	smtp.ehlo()
	smtp.starttls()
	smtp.login(username, password)

	subject = "Weekly Tips!"
	content = messages[title]
	msg = message(subject, content)

	smtp.sendmail(from_addr=username, to_addrs=recipients, msg=msg.as_string())	
	smtp.quit()

def dietMail():	
	mail("diet")

def workoutMail():
	mail("workout")

def yogaMail():
	mail("yoga")

schedule.every().monday.at("10:00").do(dietMail)
schedule.every().wednesday.at("10:00").do(workoutMail)
schedule.every().friday.at("10:00").do(yogaMail)

while True:
	schedule.run_pending()
	time.sleep(1)