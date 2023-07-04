from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from base64 import b64encode

db = SQLAlchemy()
ma = Marshmallow()


class Admins(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)


class Details(db.Model):
    __tablename__ = 'details'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False)
    address = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text, nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    photo = db.Column(db.LargeBinary, nullable=False)
    dni_front = db.Column(db.LargeBinary, nullable=False)
    dni_back = db.Column(db.LargeBinary, nullable=False)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    surname = db.Column(db.Text, nullable=False)
    dni = db.Column(db.Text, nullable=False)
    valid = db.Column(db.Boolean, nullable=False)
    id_details = db.Column(db.Integer, db.ForeignKey(
        'details.id'), nullable=False)


class AdminSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password')


admin_schema = AdminSchema()
admins_schema = AdminSchema(many=True)


class DetailSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'address', 'phone',
                  'birthdate', 'photo', 'dni_front', 'dni_back')

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


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'name', 'surname',
                  'dni', 'valid', 'id_details')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
