from db.run_sql import run_sql
from models.country import Country
from models.traveler import Traveler

def save(traveler):
    sql = "INSERT INTO travelers( name ) VALUES ( ? ) RETURNING id"
    values = [traveler.name]
    results = run_sql( sql, values )
    traveler.id = results[0]['id']
    return traveler

def select_all():
    travelers = []

    sql = "SELECT * FROM traveler"
    results = run_sql(sql)
    
    for row in results:
        traveler = Traveler(row['name'], row['category'], row['id'])
        travelers.append(traveler)
    return travelers





