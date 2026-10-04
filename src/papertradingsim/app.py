"""Flask application factory for the paper-trading simulator."""

from flask import Flask, jsonify

from .config import Config


def create_app(test_config: dict | None = None) -> Flask:
    """Create and configure the Flask application."""

    app = Flask(__name__)
    app.config.from_object(Config)

    if test_config is not None:
        app.config.update(test_config)

    @app.get("/health")
    def health():
        return jsonify(status="ok", service="papertradingsim")

    return app
