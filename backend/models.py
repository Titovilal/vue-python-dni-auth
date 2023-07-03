from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from base64 import b64encode

db = SQLAlchemy()
ma = Marshmallow()

class Users(db.Model):
    username = db.Column(db.String(64), primary_key=True)
    password = db.Column(db.String(64))
    id_details = db.Column(db.Integer, db.ForeignKey('details.id'))
    admin = db.Column(db.Integer)

    def __init__(self, username, password, id_details, admin):
        self.username = username
        self.password = password
        self.id_details = id_details
        self.admin = admin

class UserSchema(ma.Schema):
    class Meta:
        fields = ('username', 'password', 'id_details', 'admin')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    surname = db.Column(db.Text)
    email = db.Column(db.Text)
    address = db.Column(db.Text)
    phone = db.Column(db.Text)
    birthdate = db.Column(db.Date)
    photo = db.Column(db.LargeBinary)
    dni_front = db.Column(db.LargeBinary)
    dni_back = db.Column(db.LargeBinary)
    is_validated = db.Column(db.Boolean)

    def __init__(self, name, surname, email, address, phone, birthdate, photo, dni_front, dni_back, is_validated):
        self.name = name
        self.surname = surname
        self.email = email
        self.address = address
        self.phone = phone
        self.birthdate = birthdate
        self.photo = photo
        self.dni_front = dni_front
        self.dni_back = dni_back
        self.is_validated = is_validated

from base64 import b64encode

class DetailSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'surname', 'email', 'address', 'phone', 'birthdate', 'photo', 'dni_front', 'dni_back', 'is_validated')

    # Created due to problems with marshmallow schema
    def dump(self, obj, many=None, **kwargs):
        if obj.photo:
            obj.photo = b64encode(obj.photo).decode('utf-8')
        if obj.dni_front:
            obj.dni_front = b64encode(obj.dni_front).decode('utf-8')
        if obj.dni_back:
            obj.dni_back = b64encode(obj.dni_back).decode('utf-8')
        return super().dump(obj, many=many, **kwargs)


detail_schema = DetailSchema()
details_schema = DetailSchema(many=True)
