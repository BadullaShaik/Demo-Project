from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/hello/<name>')
def hello_msg(name):
	return render_template('hello.html',msg=name)

if __name__=='__main__':
	
	app.debug=True
	app.run('0.0.0.0',port=8000)