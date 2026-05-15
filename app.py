from flask import Flask, jsonify
from db import get_connection

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Product Inventory API",
        "version": "1.0"
    }), 200

@app.route("/health", methods=["GET"])
def health_check():
    """Check if the database connection works."""
    conn = get_connection()
    if conn and conn.is_connected():
        conn.close()
        return jsonify({"status": "ok", "database": "connected"}), 200
    return jsonify({"status": "error", "database": "disconnected"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)