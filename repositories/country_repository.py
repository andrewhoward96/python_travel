

from db.run_sql import run_sql
from models.country import Country
from models.traveler import Traveler

import repositories.traveler_repository as traveler_repository
import repositories.country_repository as country_repository
import repositories.visit_repository as visit_repository


def save(country):
    sql = "INSERT INTO countries(country, city) VALUES ( ?, ? ) RETURNING id"
    values = [country.country, country.city]
    results = run_sql( sql, values )
    country.id = results[0]['id']
    return country

def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['country'], row['city'], row['id'])
        countries.append(country)
    return countries

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def select(id):
    location = None
    sql = "SELECT * FROM countries WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        location = Country(result['country'], result['city'], result['id'])
    return location

def travelers(country):
    travelers = []
    sql = "SELECT travelers.* FROM travelers INNER JOIN visits ON travelers.id = visits.traveler_id WHERE country_id = ? "
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        traveler = Traveler(row['name'], ['id'])
        travelers.append(traveler)
    return travelers

def update(country):
    sql = "UPDATE countries SET (country, city) = (?,?) WHERE id = ?"
    values = [country.country, country.city, country.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM countries WHERE id = ?"
    values = [id]
    run_sql(sql, values)
    