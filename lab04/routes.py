from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input
import csv

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        zID = int(request.form["zID"])
        description = request.form["desc"]

        with open('example.csv','a') as csv_out:
			writer = csv.writer(csv_out)
			writer.writerow([name, zID, description])

        return redirect(url_for("hello"))
    return render_template("index.html")

@app.route("/Hello")
def hello():
	with open('example.csv','r') as csv_in:
		reader = list(csv.reader(csv_in))
    	return render_template("hello.html", all_users=reader)
    	
@app.route("/Hello/<user>")
def userdetails(user):
	with open('example.csv', 'r') as csv_in:
		reader = csv.reader(csv_in)
		for name in reader:
			if name[0] == user:
				return render_template("user.html", user=name)
		
	
    

