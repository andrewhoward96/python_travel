from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.country_controller import countries
from models.visit import Visit
import repositories.visit_repository as visit_repository
import repositories.traveler_repository as traveler_repository
import repositories.country_repository as country_repository

visits_blueprint = Blueprint("visits", __name__)

@visits_blueprint.route("/visits")
def visits():
    visits = visit_repository.select_all() 
    return render_template("visits/index.html", visits = visits)


@visits_blueprint.route("/visits/new", methods=['GET'])
def new_task():
    travelers = traveler_repository.select_all()
    countries = country_repository.select_all()
    return render_template("visits/new.html", travelers = travelers, countries = countries)
