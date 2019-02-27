from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'ハローワールド!!'


@app.route('/hello_world_json', methods=['GET'])
def hello_world_json():
    return jsonify({"aa": "bb"})


if __name__ == '__main__':
    app.run()
