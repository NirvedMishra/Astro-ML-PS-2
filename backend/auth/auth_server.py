import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_session import Session
from routes.auth_routes import auth_blueprint
from config import Config
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

print("CLIENT_URI:", os.getenv("CLIENT_URI"))


cors_options = {
    "supports_credentials": True,
    "origins": [f"{os.getenv('CLIENT_URI')}"],  # Your HTTP frontend
    "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    "allow_headers": ["Content-Type", "Authorization", "X-Requested-With"],
}
CORS(app, **cors_options)

# Load configuration
app.config.from_object(Config)

# Initialize session
Session(app)

# Register Blueprints
app.register_blueprint(auth_blueprint, url_prefix="/auth")


# Error handling
@app.errorhandler(404)
def not_found_error(error):
    return {"error": {"status": 404, "message": "Page Not Found!"}}, 404


@app.errorhandler(500)
def internal_server_error(error):
    return {"error": {"status": 500, "message": "Internal Server Error!"}}, 500


if __name__ == "__main__":
    app.run(debug=True, port=8080)
