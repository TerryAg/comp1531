from flask import Flask, redirect, render_template, request, url_for
from server import app
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

def bubblesort(nums):
	# Sorts the list of nums with Bubblesort
	with open('bubblesorting.csv', 'w') as bubbles:
		bubbles.write(', '.join(map(str, nums))+'\n')
		while True:
			for i, j in list(enumerate(nums))[:-1]:
				if j > nums[i+1]:
					print("Swapping %d and %d --", j, nums[i+1], i)
					nums[i] = nums[i+1] # modifying a list while iterating through it so it won't work
					nums[i+1] = j

					bubbles.write(', '.join(map(str, nums))+'\n')
			else:
				break