from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country

from repositories import country_repository, traveler_repository, visit_repository


countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all() 
    return render_template("countries/index.html", countries = countries)

@countries_blueprint.route("/countries/<id>")
def show(id):
    country = country_repository.select(id)
    travelers= country_repository.travelers(country)
    return render_template("countries/show.html", country=country, travelers=travelers)


# RESTful CRUD Routes

# INDEX
# GET '/tasks'
@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all() # NEW
    return render_template("countries/index.html", all_countries = countries)


# NEW
# GET '/tasks/new'

# CREATE
# POST '/tasks'

# SHOW
# GET '/tasks/<id>'

# EDIT
# GET '/tasks/<id>/edit'

# UPDATE
# PUT '/tasks/<id>'

# DELETE
# DELETE '/tasks/<id>'
