from flask import Flask, jsonify
from flask_login import LoginManager, login_user, login_required, current_user

from user import User

app = Flask(__name__)

app.secret_key = 'secret-key'

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/login', methods=['POST'])
def login():
    login_user(User(3))
    return ""


@app.route('/user', methods=['GET'])
@login_required
def dashboard():
    return jsonify({
                "id": current_user.user_id,
            })


@login_manager.user_loader
def load_user(user_id):
    return User(user_id=user_id)
