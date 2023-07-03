from flask import Flask
from config import *
from models import *
from views import *
from views import views_bp

app = Flask(__name__)

app.register_blueprint(views_bp)
app.config.from_object('config')

db.init_app(app)
ma.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
