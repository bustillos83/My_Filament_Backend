from exts import db


"""


class Filament:
    id: int primary key
    name: str
    type: str
    color: str

"""


class Filament(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    type = db.Column(db.String(), nullable=False)
    color = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Filament {self.name}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, name, type, color):
        self.name = name
        self.type = type
        self.color = color

        db.session.commit()

# user model


"""
class User:
    id: integer
    username: string
    email: string
    password: string
"""


class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def __repr__(self):
