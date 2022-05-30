
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.traveler import Traveler
import repositories.visit_repository as visit_repository
import repositories.traveler_repository as traveler_repository
import repositories.country_repository as country_repository


travelers_blueprint = Blueprint("travelers", __name__)

@travelers_blueprint.route("/travelers")
def travelers():
    travelers = traveler_repository.select_all() 
    return render_template("travelers/index.html", travelers = travelers)

@travelers_blueprint.route("/travelers/show", methods=['GET'])
def new_task():
    travelers = traveler_repository.select_all()
    countries = country_repository.select_all()
    return render_template("travelers/show.html", travelers = travelers, countries = countries)

# RESTful CRUD Routes

# INDEX
# GET '/travelers'
@travelers_blueprint.route("/travelers")
def travelers():
    travelers = traveler_repository.select_all() # NEW
    return render_template("travelers/index.html", all_travelers = travelers)


# NEW
# GET '/tasks/new'
@travelers_blueprint.route("/travelers/new", methods=['GET'])
def new_task():
    countries = country_repository.select_all()
    return render_template("travelers/new.html", countries = countries)


# CREATE
# POST '/tasks'
@travelers_blueprint.route("/travelers", methods=['POST'])
def create_task():
    traveler = Traveler(request.form['name'], request.form['country'])
    traveler_repository.insert(traveler)
    return redirect("/travelers")


# SHOW
# GET '/tasks/<id>'
@travelers_blueprint.route("/travelers/<id>", methods=['GET'])
def show_task(id):
    traveler = traveler_repository.select(id)
    return render_template("travelers/show.html", traveler = traveler)
    

# EDIT
# GET '/tasks/<id>/edit'

# UPDATE
# PUT '/tasks/<id>'

# DELETE
# DELETE '/tasks/<id>'