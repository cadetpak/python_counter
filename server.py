from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
#NEED this line to run sessions
app.secret_key = "SECrettttTT"

@app.route('/')
def index():  
	session['count'] = 0
	return redirect('/increase')

@app.route('/increase')
def add_one():
	session['count'] += 1
	return render_template("index.html", count = session['count'])

@app.route('/plustwo', methods=['POST'])
def increase(): 
	session['count'] += 1
	return redirect('/increase')

@app.route('/reset', methods=['POST'])
def reset(): 
	session.clear()
	return redirect('/')

app.run(debug=True)