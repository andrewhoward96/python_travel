from db.run_sql import run_sql
from models.country import Country
from models.traveler import Traveler

import repositories.traveler_repository as traveler_repository
import repositories.country_repository as country_repository
import repositories.visit_repository as visit_repository




def save(traveler):
    sql = "INSERT INTO travelers( name, category ) VALUES ( ?,? ) RETURNING id"
    values = [traveler.name, traveler.category]
    results = run_sql( sql, values )
    traveler.id = results[0]['id']
    return traveler

def select_all():
    travelers = []

    sql = "SELECT * FROM travelers"
    results = run_sql(sql)
    
    for row in results:
        traveler = Traveler(row['name'], row['category'], row['id'])
        travelers.append(traveler)
    return travelers





