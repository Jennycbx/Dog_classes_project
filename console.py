import pdb
from models.member import Member
from models.session import Session
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.session_repository as session_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
session_repository.delete_all()
member_repository.delete_all()

member1 = Member('Charlie', 8, 'Hound')
member_repository.save(member1)

member2 = Member('Cooper', 2, 'Spaniel')
member_repository.save(member2)

member3 = Member('Jess', 12, 'Retriever')
member_repository.save(member3)

member4 = Member('Archie', 1, 'Retriever')
member_repository.save(member4)

session1 = Session('Obedience', 'Monday 26th', 30, 'All')
session_repository.save(session1)

session2 = Session('Agility', 'Tuesday 27th', 60, 'All')
session_repository.save(session2)

session3 = Session('Puppy', 'Wednesday 28th', 30, 'All')
session_repository.save(session3)

session4 = Session('Scent work', 'Thursday 29th', 60, 'Hound')
session_repository.save(session4)

booking1 = Booking(member1, session4)
booking_repository.save(booking1)

booking2 = Booking(member4, session3)
booking_repository.save(booking2)

booking3 = Booking(member3, session2)
booking_repository.save(booking3)

booking4 = Booking(member2, session1)
booking_repository.save(booking4)


pdb.set_trace()


