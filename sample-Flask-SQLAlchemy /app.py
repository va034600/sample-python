import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample_db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)

    def __repr__(self):
        return "<User(id='%s', name='%s', age='%s')>" % (self.id, self.name, self.age)


class UserDtoJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        return {'name1': obj.name, 'age': obj.age}


@app.route("/")
def get_users():
    users = User.query.filter(or_(User.id == 1, User.id == 2)).all()
    return json.dumps(users, cls=UserDtoJSONEncoder)
