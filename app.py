from flask import Flask, jsonify
from flask_cors import CORS
from api.candidate_api import candidate_api


app = Flask(__name__)
CORS(app)
app.register_blueprint(candidate_api, url_prefix="/api")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
