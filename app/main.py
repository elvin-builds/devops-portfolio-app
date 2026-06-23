from flask import Flask, jsonify
import os
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({
        "app": "devops-portfolio",
        "version": os.getenv("APP_VERSION", "0.1.0"),
        "environment": os.getenv("APP_ENV", "development"),
        "debug": os.getenv("APP_DEBUG", "false"),
        "timestamp": datetime.datetime.utcnow().isoformat()
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/ready")
def ready():
    return jsonify({"status": "ready"}), 200


if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", 5000))
    debug = os.getenv("APP_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
