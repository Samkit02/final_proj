from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sjdfgyudfg7634ydgwid78r3re48ryf78wrc7e8rcdc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/final_pro'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from final_pro import route
