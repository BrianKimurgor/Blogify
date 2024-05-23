from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = '8c712967323ee4bbec8f02144f1373dd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from Blogify.model import User


@login_manager.user_loader
def load_user(user_id):
    # Assuming you have a User model with an id column
    return User.query.get(int(user_id))



from Blogify import route, forms


login_manager.init_app(app)
