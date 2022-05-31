
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