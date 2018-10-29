from flask import Flask,render_template
import psycopg2

app=Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/register')
def register():
	return render_template('student.html')


if __name__=='__main__':
	app.debug=True
	app.run(host='0.0.0.0',port=8000)
