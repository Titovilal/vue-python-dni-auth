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

    if user := Users.query.filter_by(
        username=username, password=password
    ).first():
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'})


@views_bp.route('/login-admin', methods=['POST'])
def loginAdmin():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if admin := Admins.query.filter_by(
        username=username, password=password
    ).first():
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'})


@views_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    new_detail = Details()
    db.session.add(new_detail)
    db.session.flush()

    new_user = Users(username=username, password=password,
                     id_details=new_detail.id)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'success': True})
    except:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'Error registering user'})


# PUT Routes


@views_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = Users.query.get(id)

    if not user:
        return jsonify({'success': False, 'message': 'User not found'})

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    name = data.get('name')
    surname = data.get('surname')
    dni = data.get('dni')

    if username:
        user.username = username
    if password:
        user.password = password
    if name:
        user.name = name
    if surname:
        user.surname = surname
    if dni:
        user.dni = dni

    db.session.commit()

    return jsonify({'success': True})


@views_bp.route('/users/<int:id>/details', methods=['PUT'])
def update_user_details(id):
    user = Users.query.get(id)

    if not user:
        return jsonify({'success': False, 'message': 'User not found'})

    details = Details.query.get(user.id_details)

    if not details:
        return jsonify({'success': False, 'message': 'Details not found'})

    data = request.get_json()
    email = data.get('email')
    address = data.get('address')
    phone = data.get('phone')
    birthdate = data.get('birthdate')

    if email:
        details.email = email
    if address:
        details.address = address
    if phone:
        details.phone = phone
    if birthdate:
        details.birthdate = birthdate

    db.session.commit()

    return jsonify({'success': True})


@views_bp.route('/users/<int:id>/validate', methods=['PUT'])
def validate_user(id):
    user = Users.query.get(id)

    if not user:
        return jsonify({'success': False, 'message': 'User not found'})

    data = request.get_json()
    valid = data.get('valid')

    if valid is not None:
        user.valid = valid

    db.session.commit()

    return jsonify({'success': True})
