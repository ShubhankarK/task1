from flask import Flask, request, render_template, abort, make_response
import simplejson as json
import requests, sys


app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello-World - Shubhankar'

@app.route('/authors')
def authors():
	req1 = requests.get('https://jsonplaceholder.typicode.com/users')
	req2 = requests.get('https://jsonplaceholder.typicode.com/posts')
	json_object1=req1.json()
	json_object2=req2.json()
	return render_template('task1-2.html',authors=json_object1,posts=json_object2)	

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
		user_name = 'Shubhankar'
		user_age = '20'
		resp = make_response(render_template('task1-3.html'))
		resp.set_cookie('Username', user_name)
		resp.set_cookie('Age', user_age)
		return resp

@app.route('/getcookies')
def getcookie():
	username = request.cookies.get('Username')
	age = request.cookies.get('Age')
	return 'Welcome ' + username + '<br>Your Age is ' + age

@app.route('/robots.txt')
def robots_deny():
	abort(403)

@app.route('/html')
def html():
	return render_template('task1-6.html')

@app.route('/input')
def student_data():
	return render_template('task1-7.html')

@app.route('/output', methods = ['POST', 'GET'])
def display():
   if request.method == 'POST':
       username = request.form['name']
       print(username, file=sys.stdout)
   return 'Your Name is displayed on the Terminal.'

if (__name__) == '__main__':
	app.run(debug = True)