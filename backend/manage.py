from flask.cli import FlaskGroup

from core import app, db
from core.src.models import *


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.commit()
    print(db.get_tables_for_bind())

@cli.command("drop_db")
def drop_db():
    with app.app_context():
        db.drop_all()
        db.session.commit()

@cli.command("seed_db")
def seed_db():
    with app.app_context():
        db.session.add(User(username="michael", password="@mherman.org"))
        db.session.commit()


if __name__ == "__main__":
    cli()
