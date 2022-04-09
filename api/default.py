from flask import Blueprint, jsonify, make_response
default_api = Blueprint('default_api', __name__)

@default_api.route("", methods=['GET'])
def getIndex():
    return make_response(jsonify({"message": "Running"}), 200)
