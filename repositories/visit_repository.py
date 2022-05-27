from db.run_sql import run_sql
from models.visit import Visit
import repositories.traveler_repository as traveler_repository
import repositories.location_repository as location_repository



def save(visit):
    sql = "INSERT INTO visits ( traveler_id, location_id) VALUES ( ?, ?) RETURNING id"
    values = [visit.traveler.id, visit.location.id]
    results = run_sql( sql, values )
    visit.id = results[0]['id']
    return visit
