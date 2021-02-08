class Booking:

    def __init__( self, member, session, review, id = None ):
        self.member = member
        self.session = session
        self.review = review
        self.id = id