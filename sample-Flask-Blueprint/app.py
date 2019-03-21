from flask import Flask
from sub1.app import sub1
from sub2.app import sub2

app = Flask(__name__)

app.register_blueprint(sub1, url_prefix='/sub1')
app.register_blueprint(sub2, url_prefix='/sub2')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
