from db.run_sql import run_sql
from models.session import Session
from models.member import Member

def save(member):
    sql = "INSERT INTO members (name, age, type) VALUES (%s, %s, %s) RETURNING *"
    values = [user.name]
    results = run_sql( sql, values )
    user.id = results[0]['id']
    return member


def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row[age], row[type], row['id'])
        users.append(user)
    return users


