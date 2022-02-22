import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_SECRET_KEY = '0sn6ldj83kn5l6bh'

# S3_BUCKET = 'rudolfkiss.com'
# S3_REGION = 'eu-central-1'
# S3_KEY = os.getenv('AWS_ACCES_KEY')
# S3_SECRET = os.getenv('AWS_ACCES_SECRET')