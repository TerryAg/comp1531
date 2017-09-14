from flask import Flask, redirect, render_template, request, url_for
from server import app
from math import sqrt, log, sin, cos, tan
calc_input = ''
past_input = ''
stack = []
curr_stack = 0


@app.route('/', methods=['GET', 'POST'])
def index():
	global calc_input
	global stack
	global curr_stack
	global past_input
	if request.method == "POST":
		user_input = request.form["calc"]
		if user_input == '=':
			try:
				result = str(eval(calc_input))
			except (ValueError, SyntaxError):
				result = 'err'
				calc_input = ''
			if result != 'err':
				if len(stack) < 5:
					stack.append(result)
				else:
					stack = stack[1:] + [result]
			curr_stack = 0
			return render_template("index.html", input=str(result))
		elif user_input == 'C' or user_input == 'CE':
			calc_input = ''
		elif user_input == '<':
			if curr_stack == 0:
				past_input = calc_input
				curr_stack = -1
			else:
				if -5 <= curr_stack <= -1:
					calc_input = stack[curr_stack]
					curr_stack -= 1
				elif curr_stack == 0:
					calc_input = past_input
					curr_stack = -1 # so we can move
		elif user_input == '>':
			if -5 <= curr_stack <= -1:
				calc_input = stack[curr_stack]
				curr_stack += 1
			elif curr_stack == 0:
				calc_input = past_input
		else:
			calc_input += request.form["calc"]
	return render_template("index.html", input=calc_input)