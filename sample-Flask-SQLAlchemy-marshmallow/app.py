from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample_db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)

    def __repr__(self):
        return "<User(id='%s', name='%s', age='%s')>" % (self.id, self.name, self.age)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


@app.route("/")
def hello():
    users = User.query.all()
    return jsonify(UserSchema(many=True).dump(users).data)
