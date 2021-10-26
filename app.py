from flask import Flask, jsonify, request

from games import games

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == 'POST':
		print(f'{request.json}')
	return jsonify({"games": games})