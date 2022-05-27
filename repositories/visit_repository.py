from db.run_sql import run_sql
from models.visit import Visit
import repositories.user_repository as user_repository
import repositories.location_repository as location_repository


def save(visit):
    sql = "INSERT INTO visits ( user_id, location_id, review ) VALUES ( ?, ?, ? ) RETURNING id"
    values = [visit.user.id, visit.location.id, visit.review]
    results = run_sql( sql, values )
    visit.id = results[0]['id']
    return visit
