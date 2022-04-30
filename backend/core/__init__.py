from flask import Flask, send_from_directory
from flask_cors import CORS

from core.src.models import db
from core.src.models import *
from core.src.routes import routes_bp


app = Flask(__name__)
app.config.from_object("core.config.Config")
db.init_app(app)
CORS(app)

app.register_blueprint(routes_bp)


    
@app.route("/static/<filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)
    # return f'{app.config["STATIC_FOLDER"]}'

# @app.route("/static")
# def static():
#     # return send_from_directory(app.config["STATIC_FOLDER"], filename)
#     return f'{app.config["STATIC_FOLDER"]}'