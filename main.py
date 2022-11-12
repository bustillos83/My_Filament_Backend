from flask import Flask
from flask_restx import Api
from models import Filament, User
from flask_jwt_extended import JWTManager
from exts import db
from flask_migrate import Migrate
from filaments import filament_ns
from auth import auth_ns





def create_app(config):

    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    migrate = Migrate(app, db)
    JWTManager(app)

    api = Api(app, doc='/docs')

    # Models
    api.add_namespace(filament_ns)
    api.add_namespace(auth_ns)

    @app.shell_context_processor
    def make_shell_context():
        return {
            "db": db,
            "Filament": Filament,
            "user": User

        }

    return app
