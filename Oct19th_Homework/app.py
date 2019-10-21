from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

db = SQLAlchemy(app)

ma = Marshmallow(app)

class Species(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    species = db.Column(db.Integer(), unique=False)
    strength = db.Column(db.Integer(), unique=False)
    speed = db.Column(db.Integer(), unique=False)
    intelligence = db.Column(db.Integer(), unique=False)

    def __init__(self, species, strength, speed, intelligence):
        self.species = species
        self.strength = strength
        self.speed = speed
        self.intelligence = intelligence

class SpeciesSchema(ma.Schema):
    class Meta:
        fields = ('species', 'strength', 'speed', 'intelligence')

species_schema = SpeciesSchema()
species_multiple_schema = SpeciesSchema(many=True)

#ENDPOINT: New Species
@app.route('/species', methods=['POST'])
def add_species():
    species = request.json['species']
    strength = request.json['strength']
    speed = request.json['speed']
    intelligence = request.json['intelligence']

    new_species = Species(species, strength, speed, intelligence)
    db.session.add(new_species)
    db.session.commit()

    species = Species.query.get(new_species.id)

    return species_schema.jsonify(species)

#ENDPOINT: Querying ALl Species
@app.route('/species', methods=["GET"])
def get_species_multiple():
    all_species = Species.query.all()
    result = species_schema.dump(all_species)
    return jsonify(result)

#ENDPOINT: Querying a Single Species
@app.route("/species/<id>", methods=["GET"])
def get_species(id):
    species = Species.query.get(id)
    return species_schema.jsonify(species)

if __name__ == '__main__':
    app.run(debug=True)