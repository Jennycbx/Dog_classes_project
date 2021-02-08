from db.run_sql import run_sql
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

def save(booking):
    sql = "INSERT INTO bookings (member_id, session_id, review) VALUES ( %s, %s, %s ) RETURNING id"
    values = [booking.member.id, booking.session.id, visit.review]
    results = run_sql( sql, values )
    visit.id = results[0]['id']
    return visit

def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        session = session_repository.select(row['session_id'])
        booking = Booking(member, session, row['review'], row['id'])
        bookings.append(booking)
    return bookings

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)