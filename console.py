import pdb
from models.member import Member
from models.session import Session
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.session_repository as session_repository
import repositories.booking_repository as booking_repository

member1 = Member('Charlie', 8, 'Hound')
member_repository.save(member1)

member2 = Member('Cooper', 2, 'Spaniel')
member_repository.save(member2)

member3 = Member('Jess', 12, 'Retriever')
member_repository.save(member3)

member4 = Member('Archie', 1, 'Retriever')
member_repository.save(member4)

session1 = Session('Obedience', 30, 'All')
session_repository.save(session1)

session2 = Session('Agility', 60, 'All')
session_repository.save(session2)

session3 = Session('Puppy', 30, 'All')
session_repository.save(session3)

session4 = Session('Scent work', 60, 'Hound')
session_repository.save(session4)

booking1 = Booking(member1, session4, 'Had a great time harnessing his natural ability.')
booking_repository.save(booking1)

booking2 = Booking(member4, session3, 'He was knackered at the end but had lots of fun!')
booking_repository.save(booking2)

booking3 = Booking(member3, session2, 'Felt like the other owners were getting impatient waiting for my old girl. Should do senior agility.')
booking_repository.save(booking3)

booking4 = Booking(member2, session1, 'Cooper found it hard to focus with all the other dogs but it will be something to work on.')
booking_repository.save(booking4)


pdb.set_trace()