from flask import jsonify, Blueprint
# from core.src.helpers import get_column_names
from core.src.models import *

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/send')
def member():
    return jsonify({'lakdsfakdf':{'id': 1,
                                    'name':'Vasya',
                                    'description':'Sobaka', 
                                },
                    'sdvhsdflkbv': {'id': 2,
                                    'name':'Dmitri',
                                    'description':'Kot', 
                                },
                    })

@routes_bp.route('/create')
def create_test_user():
    username = 'Test_user'
    password = 'Test_password'
    new_user = User(username = username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return 'Created'

@routes_bp.route('/show')
def show_user():
    data = db.session.query(User).all()
    column_names = User.__table__.columns.keys()
    res = {}
    for id, element in enumerate(data):
        res[id] = {column: getattr(element, column) for column in column_names}
    res = jsonify(res)
    return res
    