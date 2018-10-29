
from flask import Flask, request, redirect, url_for
import psycopg2

app = Flask(__name__)

def MyDBConn():
	con=psycopg2.connect(database="sample")
	c=con.cursor()
	#c.execute("insert into simple values('123','badulla')")
	rollno=raw_input("Enter Rollno:")
	name=str(raw_input("Enter Name:"))
	c.execute("insert into simple values({},'{}')".format(rollno,name))
	con.commit()
	if c:
		print("Inserted successfully")
	else:
		print("Sorry,Try again")
	con.close()
	

def Retrive():
	con=psycopg2.connect(database="sample")
	c=con.cursor()
	c.execute("select * from simple")
	print(c.fetchall())
	con.close()



if __name__ == '__main__':
	MyDBConn()
	Retrive()