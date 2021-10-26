from flask import Flask, jsonify, request, Response
from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId
from pymongo.collection import ReturnDocument

client = MongoClient()
db = client["python-db"]

app = Flask(__name__)

# Get games
@app.route("/games", methods=["GET"])
def get_games():
	games = db.games
	game = games.find()
	response = json_util.dumps(game)
	return Response(response, mimetype="application/json")


# Create game
@app.route("/games", methods=["POST"])
def create_game():
	obj = request.json
	games = db.games
	games.insert_one(obj)
	return jsonify({"Game": "Created"})


# Update game
@app.route("/games/<string:id>", methods=["PUT"])
def update_game(id):
	obj = request.json
	games = db.games
	objDb = games.find_one_and_update(
					{"_id": ObjectId(id)},
					{"$set": {"name": obj["name"]}},
					return_document=ReturnDocument.AFTER
				)
	response = json_util.dumps(objDb)
	return Response(response, mimetype="application/json")


# Delete game
@app.route("/games/<string:id>", methods=["DELETE"])
def delete_game(id):
	games = db.games
	games.delete_one({"_id": ObjectId(id)})
	response = jsonify({"message": "Game:" + id + "deleted"})
	response.status_code = 204
	return response