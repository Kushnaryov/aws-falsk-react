import os
from secrets import token_urlsafe


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = token_urlsafe(16)

# S3_BUCKET = 'rudolfkiss.com'
# S3_REGION = 'eu-central-1'
# S3_KEY = os.getenv('AWS_ACCES_KEY')
# S3_SECRET = os.getenv('AWS_ACCES_SECRET')