from db.run_sql import run_sql
from models.location import Location
from models.user import User

def save(user):
    sql = "INSERT INTO users( name ) VALUES ( ? ) RETURNING id"
    values = [user.name]
    results = run_sql( sql, values )
    user.id = results[0]['id']
    return user
