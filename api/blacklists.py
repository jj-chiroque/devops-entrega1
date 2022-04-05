from flask import Blueprint, request, jsonify, make_response
from database.db_connection import DBConnection
from injector import inject
from model.blacklist_model import Blacklist, convertToList, pydantic_parser

blacklists_api = Blueprint('blacklists_api', __name__)

def validateToken(request):
    headers = request.headers
    token = headers.get("Authorization")        
    if token:
        if token == "DEVOPS":
            return True    
    return False

@blacklists_api.route("", methods=['POST'])
@inject
def post(dbConnection: DBConnection):

    if not validateToken(request):
        return make_response({"message": "Missing or invalid token"}, 403)
    
    email = request.json["email"]
    app_uuid = request.json["app_uuid"]
    blocked_reason = request.json["blocked_reason"]  
    ip_address = request.remote_addr

    print(email)
    print(app_uuid)
    print(blocked_reason)
    print(ip_address)

    newItem = Blacklist(email=email, app_uuid=app_uuid, blocked_reason=blocked_reason, ip_address=ip_address)
    dbConnection.db.session.add(newItem)
    dbConnection.db.session.commit()   

    return jsonify({"message": "blacklist was added"}), 201

@blacklists_api.route("", methods=['GET'])
@inject
def getBlacklists(dbConnection: DBConnection):
    querResult =  dbConnection.db.session.query(Blacklist).all()
    result = convertToList(querResult)
    return make_response(jsonify(result), 200)

@blacklists_api.route("/<email>", methods=['GET'])
def getByEmail(email, dbConnection: DBConnection):

    if not validateToken(request):
        return make_response({"message": "Missing or invalid token"}, 403)
        
    querResult =  dbConnection.db.session.query(Blacklist).filter(Blacklist.email == email).first()

    if querResult is None:
        return jsonify({"message": "email not found"}), 404

    else:
        result = pydantic_parser.from_orm(querResult).dict()
        return jsonify({"data": result}), 200
