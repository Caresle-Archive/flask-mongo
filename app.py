from flask import Flask, jsonify, request

from games import games

app = Flask(__name__)

# Get games
@app.route("/games", methods=["GET"])
def get_games():
	return jsonify({"games": games})


# Create game
@app.route("/games", methods=["POST"])
def create_game():
	obj = request.json
	obj["id"] = len(games) + 1
	games.append(obj)
	return jsonify(obj)


# Delete game
@app.route("/games/<int:id>", methods=["DELETE"])
def delete_game(id):
	for game in games:
		if game["id"] == id:
			games.pop(id)
	return jsonify({})