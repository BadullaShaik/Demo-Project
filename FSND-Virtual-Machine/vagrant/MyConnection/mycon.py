from flask import Flask
import psycopg2

app=Flask(__name__)
def mycon():
	cur.execute("CREATE TABLE IF NOT EXISTS STUDENTS(ROLLNO TEXT,NAME TEXT,BRANCH TEXT)")
	
	rollno=raw_input("Enter rollno : ")
	name=raw_input("Enter a name : ")
	branch =raw_input("Enter branch : ")
	cur.execute("INSERT INTO STUDENTS VALUES('?,?,?')",(rollno,name,branch))

	con.commit()
	print("ONE RECORD INSERTED")

def showall():
	cur.execute("SELECT * FROM STUDENTS")
	for rec in cur.fetchall():
		print(rec)

if __name__ == '__main__':
	con=psycopg2.connect(database='srit')
	cur=con.cursor()
	ch=0
	while ch!=3:
		ch=int(input("1.INSERT 2.SHOW 3.EXIT"))
		if ch==1:
			mycon()
		else:
			showall() 	

	