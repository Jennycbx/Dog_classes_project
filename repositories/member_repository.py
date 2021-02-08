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
        member = Member(row['name'], row[age], row[type], row['id'])
        members.append(member)
    return members


# def select(id):
#     user = None
#     sql = "SELECT * FROM users WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]

#     if result is not None:
#         user = User(result['name'], result['id'] )
#     return user


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

# def locations(user):
#     locations = []

#     sql = "SELECT locations.* FROM locations INNER JOIN visits ON visits.location_id = locations.id WHERE user_id = %s"
#     values = [user.id]
#     results = run_sql(sql, values)

#     for row in results:
#         location = Location(row['name'], row ['category'], row['id'])
#         locations.append(location)

#     return locations