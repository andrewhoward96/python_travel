from db.run_sql import run_sql
from models.traveler import Traveler
from models.city import City

import repositories.traveler_repository as traveler_repository
import repositories.visit_repository as visit_repository
import repositories.city_repository as city_repository

def save(city):
    sql = "INSERT INTO citys(city) VALUES ( ?, ? ) RETURNING id"
    values = [city.city]
    results = run_sql( sql, values )
    city.id = results[0]['id']
    return city

def select_all():
    citys = []

    sql = "SELECT * FROM citys"
    results = run_sql(sql)

    for row in results:
        city = city(row['city'], row['id'])
        citys.append(city)
    return citys

def delete_all():
    sql = "DELETE FROM citys"
    run_sql(sql)

def select(id):
    location = None
    sql = "SELECT * FROM citys WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        location = city(result['city'], result['id'])
    return location

def travelers(city):
    travelers = []
    sql = "SELECT travelers.* FROM travelers INNER JOIN visits ON travelers.id = visits.traveler_id WHERE city_id = ? "
    values = [city.id]
    results = run_sql(sql, values)

    for row in results:
        traveler = Traveler(row['name'], ['id'])
        travelers.append(traveler)
    return travelers

def update(city):
    sql = "UPDATE citys SET (city) = (?) WHERE id = ?"
    values = [city.city, city.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM citys WHERE id = ?"
    values = [id]
    run_sql(sql, values)
    