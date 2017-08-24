from flask import Flask, redirect, render_template, request, url_for
from server import app
from math import sqrt, log, sin, cos, tan
calc_input = ''

@app.route('/', methods=['GET', 'POST'])
def index():
	global calc_input
	if request.method == "POST":
		user_input = request.form["calc"]
		if user_input == '=':
			try:
				result = str(eval(calc_input))
			except (ValueError, SyntaxError):
				result = 'err'
				calc_input = ''
			return render_template("index.html", input=str(result))
		elif user_input == 'C' or user_input == 'CE':
			calc_input = ''
		else:
			calc_input += request.form["calc"]
	return render_template("index.html", input=calc_input)