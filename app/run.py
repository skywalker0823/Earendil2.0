
from __init__ import create_app, socketio

app = create_app("dev")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=3000, allow_unsafe_werkzeug=True)




# from flask import Flask, redirect, session, render_template as rt
# # from api.url import url
# # from api.short import short
# app = Flask(__name__)


# # app.register_blueprint(url)
# # app.register_blueprint(short)


# @app.route("/")
# def index():
#     return rt("index.html")




# if __name__=="__main__":
#     app.run(host="0.0.0.0",port=3000,debug=True)