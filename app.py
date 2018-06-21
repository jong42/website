from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/map')
def map_part():
	return render_template("map.html")

@app.route('/data')
def data_part():
	return render_template("data.html")

app.run(debug=True)
