from flask import Flask,url_for,request,redirect,render_template

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/done/<msg>')
def done(msg):
	return "welcome %s" %msg

@app.route('/login',methods=['POST','GET'])
def login():
	uname=request.form['uname']
	pwd=request.form['pswd']
	return redirect(url_for('done',msg=uname))



if __name__=='__main__':
	app.debug=True
	app.run(host='0.0.0.0', port=8000)