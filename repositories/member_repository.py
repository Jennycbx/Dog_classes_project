from db.run_sql import run_sql
from models.session import Session
from models.member import Member

def save(member):
    sql = "INSERT INTO members (name, age, type) VALUES (%s, %s, %s) RETURNING id"
    values = [member.name, member.age, member.type]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['age'], row['type'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['name'], result['age'], result['type'], result['id'])
    return member


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def update(member):
    sql = "UPDATE members SET (name, age, type) = (%s, %s, %s) WHERE id = %s"
    values = [member.name, member.age, member.type, member.id]
    run_sql(sql, values)

def sessions(member):
    sessions = []

    sql = "SELECT sessions.* FROM sessions INNER JOIN bookings ON bookings.session_id = sessions.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        session = Session(row['name'], row['duration'], row['type'], row['id'])
        sessions.append(session)

    return sessions