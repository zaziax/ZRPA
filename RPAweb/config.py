from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
from flask_apscheduler import APScheduler
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SECRET_KEY'] = 'sha-RPA-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/rpa'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)

socketio = SocketIO(app)

# 初始化调度器
scheduler = APScheduler()