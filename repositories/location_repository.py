from db.run_sql import run_sql
from models.location import Location
from models.user import User

def save(location):
    sql = "INSERT INTO locations(name, category) VALUES ( ?, ? ) RETURNING id"
    values = [location.name, location.category]
    results = run_sql( sql, values )
    location.id = results[0]['id']
    return location

