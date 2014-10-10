from views import db

class Property(db.Model)
    __tablename__ = "properties"
    property_id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String, nullable=False)
    bed_rooms = db.Column(db.Integer)
    bath_rooms = db.Column(db.Integer)

    def __init__(self, property_id, address, bed_rooms, bath_rooms):
        self.property_id = property_id
        self.address = address
        self.bed_rooms = bed_rooms
        self.bath_rooms = bath_rooms

    def __repr__(self):
        return '<name %r>' % (self.body)
