
from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.traveler import Traveler
import repositories.traveler_repository as traveler_repository

travelers_blueprint = Blueprint("travelers", __name__)

@travelers_blueprint.route("/travelers")
def travelers():
    travelers = traveler_repository.select_all() 
    return render_template("travelers/index.html", travelers = travelers)

@travelers_blueprint.route("/travelers/<id>")
def show(id):
    traveler = traveler_repository.select(id)
    travelers = traveler_repository.travelers(traveler)
    return render_template("travelers/show.html", traveler=traveler, travelers = travelers)
