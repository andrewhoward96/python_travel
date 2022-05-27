from db.run_sql import run_sql
from models.location import Location
from models.traveler import Traveler

def save(traveler):
    sql = "INSERT INTO travelers( name ) VALUES ( ? ) RETURNING id"
    values = [traveler.name]
    results = run_sql( sql, values )
    traveler.id = results[0]['id']
    return traveler
