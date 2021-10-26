from flask import Flask, jsonify, request

from games import games

app = Flask(__name__)

# Get games
@app.route("/games", methods=["GET"])
def get_games():
	return jsonify({"games": games})


# Create route
@app.route("/games", methods=["POST"])
def create_game():
	print(len(games))
	obj = request.json
	obj["id"] = len(games) + 1
	games.append(obj)
	return jsonify(obj)
