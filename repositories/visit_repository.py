
from db.run_sql import run_sql
from models.visit import Visit
import repositories.traveler_repository as traveler_repository
import repositories.country_repository as country_repository



def save(visit):
    sql = "INSERT INTO visits ( traveler_id, country_id) VALUES ( ?, ?) RETURNING id"
    values = [visit.traveler.id, visit.country.id]
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