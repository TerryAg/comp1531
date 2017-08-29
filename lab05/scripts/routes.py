from flask import Flask, redirect, render_template, request, url_for
from server import app
from math import sqrt, log, sin, cos, tan
calc_input = ''
stack = []
curr_stack = -1
@app.route('/', methods=['GET', 'POST'])
def index():
	global calc_input
	global stack
	global curr_stack
	if request.method == "POST":
		user_input = request.form["calc"]
		if user_input == '=':
			try:
				result = str(eval(calc_input))
			except (ValueError, SyntaxError):
				result = 'err'
				calc_input = ''
			if result != 'err':
				stack = stack[1:]
				stack.append(result)
			return render_template("index.html", input=str(result))
		elif user_input == 'C' or user_input == 'CE':
			calc_input = ''
		elif user_input == '<' and curr_stack < 0:
			stack.append(calc_input) # In case we want to go back
			try:
				calc_input = stack[curr_stack]
			except ValueError:
				pass
			curr_stack -= 1
		elif user_input == '>' and curr_stack < 0:
			calc_input = stack[curr_stack]
			curr_stack += 1
		else:
			calc_input += request.form["calc"]
	return render_template("index.html", input=calc_input)