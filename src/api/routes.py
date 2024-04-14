"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
# ?
from flask_cors import CORS
# ?
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

# create flask app
api = Blueprint('api', __name__)


# Allow CORS requests to this API
CORS(api)

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@api.route("/token", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


@api.route("/hello", methods=["GET"])
@jwt_required()
def get_hello():
    
    email = get_jwt_identity()
    dictionary = {
        "message": "hello world"
    }
    return jsonify(dictionary)



# @api.route('/hello', methods=['POST', 'GET'])
# def handle_hello():

#     response_body = {
#         "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
#     }

#     return jsonify(response_body), 200

# # (email: 'aaa@gmail.com', password: 1234)
# @api.route('/signup', methods=['POST'])
# def create_token():
#     email = request.json["email"]
#     password = request.json["password"]

# # create a new instance of user in db
#     new_user = User(email=email, password=password)
# # add it to the db
#     db.session.add(new_user)
# # push in the db
#     db.session.commit()
    
# # create the token based on the email
#     access_token= create_access_token(identity=email)


#     return jsonify(access_token), 200