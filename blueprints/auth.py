from flask_jwt_extended import create_access_token
from flask import Blueprint, request
from flask.json import jsonify
from models import User


bp = Blueprint('auth', __name__,)


@bp.route('/login', methods=['POST'])
def Login():
    if not  request.is_json:
        return jsonify(msg="Missing JSON in headers")

    _username = request.json.get('username', -1)
    _password = request.json.get('password', -1)

    if _username == -1 or _password == -1:
        return jsonify({"msg" : "Missing Something"}), 400

    try:
       user = User.get(User.username == _username)
    except:
        return jsonify({"msg" : "USER NOT FOUND"}), 404

    if user.password != _password:
        return jsonify({"msg" : "PASSWORD WRONG"}), 404
    
    access_token = create_access_token(identity=_username)
    return jsonify({"username" : _username ,"access_token" : access_token})


@bp.route('/register', methods=['POST'])
def Register():
    if not  request.is_json:
        return jsonify(msg="Missing JSON in headers")

    _username = request.json.get('username', -1)
    _password = request.json.get('password', -1)

    if _username == -1 or _password == -1:
        return jsonify({"msg" : "Missing Something"}), 400

    access_token = create_access_token(identity=_username)
    user = User(username = _username, password = _password)
    user.save()
    return jsonify({"access_token" : access_token}), 200


if __name__ == '__main__':
    bp.run()