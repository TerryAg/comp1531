from flask import Flask, redirect, render_template, request, url_for
from server import app
from bubble import bubblesort
import csv

@app.route('/', methods=['GET', 'POST'])
def index():
	# WHere the user will input numbers
	if request.method == "POST":
		numbers = map(int, request.form["nums"].split(','))
		bubblesort(numbers)
		return redirect(url_for("result"))
	return render_template("index.html")


@app.route('/result')
def result():
	# Where the results of the bubblesort will be
	with open('bubblesorting.csv', 'r') as bubbles:
		results = list(csv.reader(bubbles))
		return render_template("results.html", results=results)