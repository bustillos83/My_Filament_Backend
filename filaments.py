
from flask_restx import Namespace, Resource, fields
from models import Filament
from flask_jwt_extended import jwt_required
from flask import request

filament_ns = Namespace('filament', description="A namespace for Filaments")


# Model (Serializer)
filament_model = filament_ns.model(
    "Filamanet",
    {
        "id": fields.Integer(),
        "name": fields.String(),
        "type": fields.String(),
        "color": fields.String()

    }
)


@filament_ns.route("/hello")
class HelloResource(Resource):
    def get(self):
        return {"message": "Hello World"}


@filament_ns.route("/filaments")
class FilamentsResource(Resource):
    @filament_ns.marshal_list_with(filament_model)
    def get(self):
        """Get all Filament"""
        filaments = Filament.query.all()

        return filaments

    @filament_ns.marshal_with(filament_model)
    @filament_ns.expect(filament_model)
    @jwt_required()
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


@filament_ns.route('/filaments/<int:id>')
class FilementResource(Resource):
    @filament_ns.marshal_with(filament_model)
    def get(self, id):
        """ Get filament by id"""
        filament = Filament.query.get_or_404(id)

        return filament

# Put route
    @filament_ns.marshal_with(filament_model)
    @jwt_required()
    def put(self, id):
        """update filament by id"""

        filament_to_update = Filament.query.get_or_404(id)

        data = request.get_json()

        filament_to_update.update(
            data.get("name"), data.get("type"), data.get("color"))

        return filament_to_update

# Delete route
    @filament_ns.marshal_with(filament_model)
    @jwt_required()
    def delete(self, id):
        """delete filament by id"""

        filament_to_delete = Filament.query.get_or_404(id)

        filament_to_delete.delete()

        return filament_to_delete
