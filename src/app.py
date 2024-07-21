from flask import Flask, jsonify, request
import random

app = Flask(__name__)


@app.route('/api/test', methods=['GET'])
def api_test_get():
    random_id = random.randint(100000, 999999)
    response = {
        "resultCode": "0",
        "resultDesc": "Success",
        "data": {
            "id": random_id
        }
    }
    return jsonify(response)


@app.route('/api/test', methods=['POST'])
def api_test_post():
    req_data = request.get_json()
    if 'id' in req_data:
        return jsonify({"resultCode": "0", "resultDesc": "Success"})
    else:
        return jsonify({"resultCode": "-1", "resultDesc": "Failure: 'id' field is missing"}), 400


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
