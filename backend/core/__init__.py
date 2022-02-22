from flask import Flask
from flask_cors import CORS

from core.src.models import db
from core.src.models import *
from core.src.routes import routes_bp


app = Flask(__name__)
app.config.from_object("core.config.Config")
db.init_app(app)
CORS(app)

app.register_blueprint(routes_bp)
