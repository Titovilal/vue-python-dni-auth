from models import Admins, AdminSchema
from flask import jsonify, Blueprint
from models import Users, Details, UserSchema, DetailSchema

views_bp = Blueprint('views', __name__)


@views_bp.route('/invalid-users', methods=['GET'])
def get_invalid_users():
    users = Users.query.filter_by(valid=0).all()
    user_schema = UserSchema(many=True)
    result = user_schema.dump(users)
    return jsonify(result)


@views_bp.route('/users', methods=['GET'])
def get_users():
    users = Users.query.all()
    user_schema = UserSchema(many=True)
    result = user_schema.dump(users)
    return jsonify(result)


@views_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = Users.query.get(id)
    user_schema = UserSchema()
    result = user_schema.dump(user)
    return jsonify(result)


@views_bp.route('/users/<int:id>/details', methods=['GET'])
def get_user_details(id):
    user = Users.query.get(id)
    details = Details.query.get(user.id_details)
    detail_schema = DetailSchema()
    result = detail_schema.dump(details)
    return jsonify(result)


@views_bp.route('/admins', methods=['GET'])
def get_admins():
    admins = Admins.query.all()
    admin_schema = AdminSchema(many=True)
    result = admin_schema.dump(admins)
    return jsonify(result)


@views_bp.route('/admins/<int:id>', methods=['GET'])
def get_admin(id):
    admin = Admins.query.get(id)
    admin_schema = AdminSchema()
    result = admin_schema.dump(admin)
    return jsonify(result)
