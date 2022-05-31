
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
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



# NEW
# GET '/tasks/new'
@travelers_blueprint.route("/travelers/new", methods=['GET'])
def tasks_for_travelers():
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
    country = traveler_repository.locations(traveler)
    return render_template("travelers/show.html", traveler = traveler, countries = country)
    

# EDIT
# GET '/tasks/<id>/edit'

def edit_task(id):
    traveler = traveler_repository.select(id)
    countries = country_repository.select_all()
    return render_template("travelers/edit.html", traveler = traveler, countries = countries)

# UPDATE
# PUT '/tasks/<id>'
@travelers_blueprint.route("/travelers/<id>", methods=['PUT'])
def update_task(id):
    name = request.form['name']
    country = request.form['country']
    traveler = Traveler(name, country, id)

    traveler_repository.update(traveler)
    return redirect("/travelers")

# DELETE
# DELETE '/tasks/<id>'
@travelers_blueprint.route("/travelers/<id>/delete", methods=['POST'])
def delete_task(id):
    traveler_repository.delete(id)
    return redirect("/travelers")
    