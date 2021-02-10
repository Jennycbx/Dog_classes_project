from db.run_sql import run_sql
from models.session import Session
from models.member import Member

def save(session):
    sql = "INSERT INTO sessions(name, day, duration, type) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [session.name, session.day, session.duration, session.type]
    results = run_sql(sql, values)
    session.id = results[0]['id']
    return session


def select_all():
    sessions = []

    sql = "SELECT * FROM sessions"
    results = run_sql(sql)

    for row in results:
        session = Session(row['name'], row['day'], row['duration'], row['type'], row['id'])
        sessions.append(session)
    return sessions

def select(id):
    session = None
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        session = Session(result['name'], result['day'], result['duration'], result['type'], result['id'] )
    return session

def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM sessions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(session):
    sql = "UPDATE sessions SET (name, day, duration, type) = (%s, %s, %s, %s) WHERE id = %s"
    values = [session.name, session.day, session.duration, session.type, session.id]
    run_sql(sql, values)

def members(id):
    members = []

    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.session_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['name'], row,['age'], row['type'])
        members.append(member)

    return members