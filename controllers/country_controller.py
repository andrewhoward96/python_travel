from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country

from repositories.country_repository import country_repository
from repositories.visit_repository import visit_repository


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





# NEW
# GET '/tasks/new'
@countries_blueprint.route("/countries/new")
def new():
    return render_template("countries/new.html")


# CREATE
# POST '/tasks'
@countries_blueprint.route("/countries", methods=['POST'])
def create():
    country = Country(request.form['name'])
    country_repository.insert(country)
    return redirect("/countries")





# EDIT
# GET '/tasks/<id>/edit'
@countries_blueprint.route("/countries/<id>/edit")
def edit(id):
    country = country_repository.select(id)
    return render_template("countries/edit.html", country=country)


# UPDATE
# PUT '/tasks/<id>'
@countries_blueprint.route("/countries/<id>", methods=['PUT'])
def update(id):
    country = Country(request.form['name'])
    country_repository.update(country)
    return redirect("/countries")


# DELETE
# DELETE '/tasks/<id>'
@countries_blueprint.route("/countries/<id>", methods=['DELETE'])
def destroy(id):
    country_repository.delete(id)
    return redirect("/countries")
