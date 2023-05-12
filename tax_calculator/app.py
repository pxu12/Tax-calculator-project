from flask import Flask, request, render_template
from tax import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods = ['POST'])
def calculate():
    income = request.form["income"]
    deduction = request.form["deduction"]
    old_tax, new_tax = compare(int(income), int(deduction))
    if new_tax < old_tax:
        Higher = "Old Tax is Higher"
        Difference = old_tax - new_tax
    else: 
        Higher = "New Tax is Higher"
        Difference = new_tax - old_tax
    
    return render_template('index.html', ot=old_tax, nt=new_tax, difference=Difference, Regime=Higher)


if __name__ == '__main__':
    app.run(debug=True, port=8000)