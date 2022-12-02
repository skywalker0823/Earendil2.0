from flask import Flask, redirect, session, render_template as rt
from config import config_sets
import os
from flask_socketio import SocketIO
from dotenv import load_dotenv
socketio = SocketIO()

load_dotenv()

def create_app(config_name):
    app = Flask(__name__, static_folder="static",static_url_path="/", template_folder="templates")
    app.config.from_object(config_sets[config_name])

    from routes.api_member import api_member
    app.register_blueprint(api_member)
    @app.route("/")
    def index():
        return rt("index.html")


    socketio.init_app(app, cors_allowed_origins="*")
    return app