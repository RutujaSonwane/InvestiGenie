from flask import Flask, request, jsonify
from flask_cors import CORS
from rag_utils import get_response

app = Flask(__name__)
CORS(app)

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    user_query = data.get("query", "")
    response = get_response(user_query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
from rag_utils import get_response

app = Flask(__name__)
CORS(app)

@app.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    user_query = data.get("query", "")
    response = get_response(user_query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
