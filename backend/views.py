from flask import jsonify, Blueprint
from models import Users, Details, UserSchema, DetailSchema

views_bp = Blueprint('views', __name__)

@views_bp.route('/users', methods=['GET'])
def get_users():
    users = Users.query.all()
    user_schema = UserSchema(many=True)
    result = user_schema.dump(users)
    return jsonify(result)

@views_bp.route('/users/<string:username>', methods=['GET'])
def get_user(username):
    user = Users.query.get(username)
    user_schema = UserSchema()
    result = user_schema.dump(user)
    return jsonify(result)

@views_bp.route('/users/<string:username>/details', methods=['GET'])
def get_user_details(username):
    user = Users.query.get(username)
    details = Details.query.get(user.id_details)
    detail_schema = DetailSchema()
    result = detail_schema.dump(details)
    return jsonify(result)
