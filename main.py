from flask import Flask, request
from flask_restx import Api, Resource, fields
from config import DevConfig
from models import Filament
from exts import db

PORT = 8000

app = Flask(__name__)
app.config.from_object(DevConfig)


db.init_app(app)


api = Api(app, doc='/docs')

# Model (Serializer)
filament_model = api.model(
    "Filamanet",
    {
        "id": fields.Integer(),
        "name": fields.String(),
        "type": fields.String(),
        "color": fields.String()

    }
)


@api.route("/hello")
class HelloResource(Resource):
    def get(self):
        return {"message": "Hello World"}

# get all filaments route


@api.route("/filaments")
class FilamentsResource(Resource):
    @api.marshal_list_with(filament_model)
    def get(self):
        """Get all Filament"""
        filaments = Filament.query.all()

        return filaments

    @api.marshal_with(filament_model)
    def post(self):
        """ Add new Filament"""

        data = request.get_json()

        new_filament = Filament(
            name=data.get('name'),
            type=data.get('type'),
            color=data.get('color')


        )
        new_filament.save()

        return new_filament, 201
        pass


@api.route('/filaments/<int:id>')
class FilementResource(Resource):
    @api.marshal_with(filament_model)
    def get(self, id):
        """ Get filament by id"""
        filament = Filament.query.get_or_404(id)

        return filament

# Put route
    @api.marshal_with(filament_model)
    def put(self, id):
        """update filament by id"""

        filament_to_update = Filament.query.get_or_404(id)

        data = request.get_json()

        filament_to_update.update(
            data.get("name"), data.get("type"), data.get("color"))

        return filament_to_update

# Delete route
    @api.marshal_with(filament_model)
    def delete(self, id):
        """delete filament by id"""

        filament_to_delete = Filament.query.get_or_404(id)

        filament_to_delete.delete()

        return filament_to_delete


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Filament": Filament}


if __name__ == "__main__":
    app.run(port=PORT)
