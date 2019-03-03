from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'ハローワールド!!'


@app.route('/hello_world_json', methods=['GET'])
def hello_world_json():
    return jsonify({"aa": "bb"})


@app.route('/hello_world_get_parameter/<path_variable>', methods=['GET'])
def hello_world_get_parameter(path_variable=None):
    return jsonify({
        "path_variable": path_variable,
        "parameter_variable": request.args.get('parameter_variable')
    })


@app.route('/hello_world_post_parameter/<path_variable>', methods=['POST'])
def hello_world_post_parameter(path_variable=None):
    return jsonify({
        "path_variable": path_variable,
        "parameter_variable": request.form['parameter_variable']
    })


@app.route('/hello_world_post_parameter_json/<path_variable>', methods=['POST'])
def hello_world_post_parameter_json(path_variable=None):
    if request.headers['Content-Type'] != 'application/json':
        return jsonify(status='error'), 400

    print(request.get_json()['parameter_variable'])

    return jsonify({
        "path_variable": path_variable,
        "parameter_variable": request.get_json()['parameter_variable']
    })


if __name__ == '__main__':
    app.run()
