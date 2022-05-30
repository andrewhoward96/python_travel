
from db.run_sql import run_sql
from models.visit import Visit
import repositories.traveler_repository as traveler_repository
import repositories.country_repository as country_repository
import repositories.visit_repository as visit_repository



def save(visit):
    sql = "INSERT INTO visits ( traveler_id, country_id, visit_id) VALUES ( ?, ?, ?) RETURNING id"
    values = [visit.traveler.id, visit.country.id, visit.id]
    results = run_sql( sql, values )
    visit.id = results[0]['id']
    return visit

def select_all():
    visits = []

    sql = "SELECT * FROM visits"
    results = run_sql(sql)

    for row in results:
        visit = Visit(row['name'], row['category'], row['id'])
        visits.append(visit)
    return visits

def select(id):
    visit = None
    sql = "SELECT * FROM visits WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        completed = True if result['completed'] == 1 else False
        traveler = traveler_repository.select(result['traveler_id'])
        visit = visit(result['description'], traveler, result['duration'], completed, result['id'] )
    return visit


def delete_all():
    sql = "DELETE  FROM visits"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM visits WHERE id = ?"
    values = [id]
    run_sql(sql, values)


def update(visit):
    sql = "UPDATE visits SET (name, category, traveler_id) = (?, ?, ?) WHERE id = ?"
    values = [visit.name, visit.category, visit.traveler.id]
    run_sql(sql, values)
