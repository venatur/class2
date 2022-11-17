from app.models import *


def create_db():
    db.drop_all()
    db.create_all()


def init_db():
    create_db()
    admin = Users(
        name="Pedro"

    )
    persona = Persona(
        name = "Edwin",
        age=20
    )
    db.session.add(admin)
    db.session.add(persona)
    db.session.commit()