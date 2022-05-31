
from flask import Flask, render_template, request, redirect
from flask import Blueprint
# from controllers.country_controller import countries
from models.visit import Visit

import repositories.visit_repository as visit_repository
import repositories.traveler_repository as traveler_repository
import repositories.country_repository as country_repository

visits_blueprint = Blueprint("visits", __name__)


@visits_blueprint.route("/visits")
def visits():
    visits = visit_repository.select_all()
    return render_template("visits/index.html", visits = visits)

# NEW
# GET '/visits/new'
@visits_blueprint.route("/visits/new", methods=['GET'])
def new_visit():
    travelers = traveler_repository.select_all()
    return render_template("visits/new.html", all_travelers=travelers)


# CREATE
# POST '/visits'
@visits_blueprint.route("/visits", methods=['POST'])
def create_visit():
    visit = Visit(request.form['traveler_id'], request.form['country_id'])
    visit_repository.insert(visit)
    return redirect("/visits")



# SHOW
# GET '/visits/<id>'
@visits_blueprint.route("/visits/<id>", methods=['GET'])
def show_visit(id): 
    visit = visit_repository.select(id)
    return render_template('visits/show.html', visit = visit)

# EDIT
# GET '/visits/<id>/edit'

@visits_blueprint.route("/visits/<id>/edit", methods=['GET'])
def edit_visit(id):
    visit = visit_repository.select(id)
    travelers = traveler_repository.select_all()
    return render_template('visits/edit.html', visit = visit, all_travelers = travelers)
# UPDATE
# not using PUT due to HTML only using POST or GET '/visits/<id>'

@visits_blueprint.route("/visits/<id>", methods=['POST'])
def update_visit(id):
    name = request.form['name']
    category = request.form['category']
    # duration = request.form['duration']
    traveler_id = bool(int(request.form['traveler_id']))
    traveler = traveler_repository.select(category)  
    visit = Visit(name, traveler, traveler_id, id)

    visit_repository.update(visit)
    return redirect('/visits')


# DELETE
# DELETE '/visits/<id>'

@visits_blueprint.route("/visits/<id>/delete", methods=['POST'])
def delete_task(id):
    visit_repository.delete(id)
    return redirect('/visits')