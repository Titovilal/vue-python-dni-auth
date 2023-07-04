from models import Admins, AdminSchema
from flask import jsonify, Blueprint, request
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


@views_bp.route('/users/<string:username>', methods=['GET'])
def get_user_by_username(username):
    user = Users.query.filter_by(username=username).first()
    user_schema = UserSchema()
    result = user_schema.dump(user)
    return jsonify(result)


@views_bp.route('/admins/<string:username>', methods=['GET'])
def get_admin_by_username(username):
    admin = Admins.query.filter_by(username=username).first()
    admin_schema = AdminSchema()
    result = admin_schema.dump(admin)
    return jsonify(result)


# Post routes


@views_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Consulta la base de datos para verificar si las credenciales son válidas
    user = Users.query.filter_by(username=username, password=password).first()
    if user:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'})

