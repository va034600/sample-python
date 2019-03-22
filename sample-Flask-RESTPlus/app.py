from flask import Flask
from flask_restplus import Api

from user import user_namespace

app = Flask(__name__)
api = Api(app, version='1.0', title='Sample API', description='サンプルサンプル', doc='/doc/')

api.add_namespace(user_namespace)

if __name__ == "__main__":
    app.run()
