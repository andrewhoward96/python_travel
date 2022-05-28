from db.run_sql import run_sql
from models.country import Country
from models.traveler import Traveler

def save(country):
    sql = "INSERT INTO countries(name, category) VALUES ( ?, ? ) RETURNING id"
    values = [country.name, country.category]
    results = run_sql( sql, values )
    country.id = results[0]['id']
    return country

