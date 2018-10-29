from flask import Flask,url_for,request,redirect,render_template

app=Flask(__name__)
#print(app)
@app.route('/')
def hello():
	print("hi")

	

if __name__ == '__main__':
	#hello()
	app.run(host='0.0.0.0',port=8000)