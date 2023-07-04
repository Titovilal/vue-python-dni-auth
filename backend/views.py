from models import Admins, AdminSchema
from flask import jsonify, Blueprint, request
from models import Users, Details, UserSchema, DetailSchema, db

views_bp = Blueprint('views', __name__)


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


@views_bp.route('/users/<string:username>/details', methods=['GET'])
def get_user_details_by_username(username):
    user = Users.query.filter_by(username=username).first()
    details = Details.query.get(user.id_details)
    detail_schema = DetailSchema()
    result = detail_schema.dump(details)
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


@views_bp.route('/login-admin', methods=['POST'])
def loginAdmin():
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Consulta la base de datos para verificar si las credenciales son válidas
    admin = Admins.query.filter_by(username=username, password=password).first()
    if admin:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'})


@views_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = Users.query.get(id)
    if not user:
        return jsonify({'success': False, 'message': 'User not found'})
    user.name = data.get('name', user.name)
    user.surname = data.get('surname', user.surname)
    user.dni = data.get('dni', user.dni)
    db.session.commit()
    user_schema = UserSchema()
    result = user_schema.dump(user)
    return jsonify(result)


@views_bp.route('/users/<int:id>/details', methods=['PUT'])
def update_user_details(id):
    data = request.get_json()
    user = Users.query.get(id)
    if not user:
        return jsonify({'success': False, 'message': 'User not found'})
    details = Details.query.get(user.id_details)
    details.birthdate = data.get('birthdate', details.birthdate)
    details.email = data.get('email', details.email)
    details.address = data.get('address', details.address)
    db.session.commit()
    detail_schema = DetailSchema()
    result = detail_schema.dump(details)
    return jsonify(result)
