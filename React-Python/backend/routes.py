
from app import app, db
from flask import request, jsonify
from app import Friend  # Import Friend from app instead of backend.models

@app.route("/api/friends", methods=["GET"])  # Use capital "GET"
def get_friends():
    friends = Friend.query.all()
    result = [friend.to_json() for friend in friends]
    return jsonify(result)
