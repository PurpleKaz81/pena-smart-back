from flask import Flask, jsonify
from flask_cors import CORS
from utilities import qualifiers
import sys

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return jsonify(message='Hello, World!')

@app.route('/api/qualifiers', methods=['GET'])
def get_all_qualifiers():
    return qualifiers.get_qualifiers()


if __name__ == '__main__':
    print(sys.executable)
    app.run(debug=True)
