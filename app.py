from flask import Flask, jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from blueprints.auth import bp as Auth
from blueprints.send import bp as Send

app = Flask(__name__)
app.register_blueprint(Auth)
app.register_blueprint(Send)
jwt = JWTManager(app)

#write your config

@app.route('/', methods=['GET'])
@jwt_required()
def Main():
    return jsonify()

if __name__ == '__main__':
   app.run(debug = True)