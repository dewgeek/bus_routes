
from flask import jsonify
import re
from flask import Flask, jsonify, request, render_template, flash
app = Flask(__name__, static_folder='static', template_folder= 'templates')

app.secret_key='secret'

import pymongo
connection = pymongo.Connection()
db = connection.mydb
bus8 = db.bus8
bus_data = db.bus_data



@app.route('/home')
def sort():

	total_data = bus8.find()
	from_list = []
	to_list = []
	via = []
	via_list = []
	via_lists = []
	for i in total_data:

		from_list.append(i['from'])
		from_list.append(i['to'])

		to_list.append(i['to'])
		to_list.append(i['from'])

		via.append(i['via'])
		for j in via: 
			via_list = j.split(',')

			for k in via_list:
				to_list.append(str(k))
				from_list.append(str(k))
		

	from_list = list(set(from_list))

	to_list = list(set(to_list ))
	

	return render_template('home.html', from_data = from_list, to_data= to_list )


@app.route('/input', methods=('GET' ,'POST'))
def sorted():
	if request.method == 'POST':
		start = request.form['from']
		to = request.form['to']

		stops = 0
		bus_num = 0
		found = bus8.find({ 'from': start, 'to': to })
		if not found.count=='0':
			for i in found:
				
				stops = i['via']
				bus_num = i['bus num']

		else: bus_num = 'not found'

	return render_template('index.html', num = bus_num , stop= stops)


@app.route('/search', methods=('GET','POST') )
def search():
	
	if request.method=='POST':
		number = request.form['number']

		record = bus8.find({ 'bus num': number })
		value={}

		for i in record:
			value['number'] = i['bus num']
			value['from'] = i['from']
			value['to'] = i['to']
			value['via'] = i['via']

		return render_template('edit.html', value = value) 

	return render_template('search.html')





@app.route('/<num>', methods=['GET'])
def busnum(num):
	f = bus8.find({'bus num': num })
	for i in f:
		print i

	return 'True'


if __name__ == '__main__':
	app.run(debug=True)
