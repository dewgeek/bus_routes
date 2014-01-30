
from flask import jsonify
import re
import requests
from flask import Flask, jsonify, request, render_template, json
app = Flask(__name__, static_folder='static', template_folder= 'templates')

app.secret_key= '\xbf\xb50\x94au\x8f\xf9\se2\x1f\x93\x06(\xdf\xe4\xaf\x1f\x86k\xb3\x2fQ%1'


@app.route('/home')
def home():

	data = requests.get('http://routes1.herokuapp.com/')

	binary = data.content
	output = json.loads(binary)

	from_list = []
	to_list = []
	
	for i in output['start']:
		from_list.append(i)

	for j in output['end']:
		to_list.append(j)

	return render_template('home.html', from_data = from_list, to_data = to_list )


@app.route('/input', methods=('GET' ,'POST') )
def sorted():
	if request.method=='POST':
		start = request.form['from']
		end = request.form['to']

		url = 'http://routes1.herokuapp.com/%s/%s' %(start,end)
		data = requests.get(url)
		
		binary = data.content
		output = json.loads(binary)
		
		num = []

		for j in output['number']:
			
			num.append(j)

		num = list(set(num))
			
		return render_template('index.html', num= num)

@app.route('/edit', methods=('GET' ,'POST') )
def edit():

	if request.method=='POST':
		
		start = request.form['starts'] 
		end = request.form['end']
		number = request.form['number']
		bus_type = request.form['type']
		passes = request.form['via']  

		new = request.form.getlist('check')
		edit = request.form.getlist('edit')

		
		print new, start, end

		

	return render_template('edit.html')


	

if __name__ == '__main__':
	app.run(debug=True)
