from unittest import result
from db.run_sql import run_sql
from models.country import Country
from models.traveler import Traveler

import repositories.traveler_repository as traveler_repository
import repositories.country_repository as country_repository
import repositories.visit_repository as visit_repository




def save(traveler):
    sql = "INSERT INTO travelers( name) VALUES ( ? ) RETURNING id"
    values = [traveler.name]
    results = run_sql( sql, values )
    traveler.id = results[0]['id']
    return traveler

def select_all():
    travelers = []

    sql = "SELECT * FROM travelers"
    results = run_sql(sql)
    
    for row in results:
        traveler = Traveler(row['name'], row['id'])
        travelers.append(traveler)
    return travelers

def delete_all():
    sql = "DELETE FROM travelers"
    run_sql(sql)

def locations(traveler):
    locations = []
    sql = "SELECT countries.* from countries INNER JOIN visits ON countries.id=visits.country_id WHERE traveler_id = ?"
    values = [traveler.id]
    results = run_sql(sql, values)

    for row in results:
        location = Country(row['country'], row['city'], row['id'])
        locations.append(location)

    return locations


def select(id):
    traveler = None
    sql = "SELECT * FROM travelers WHERE id = ?"
    values = [id]
    results = run_sql(sql, values)[0]
  
    if results is not None:
        traveler = Traveler(results['name'], results['id'])
    return traveler


