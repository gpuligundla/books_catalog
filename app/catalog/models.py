from app import db
from datetime import datetime

class Publications(db.Model):
    __tablename__ = 'publications'

    id = db.Column(db.Integer, primary_key="true")
    name = db.Column(db.String(100),unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "The name of Publication is {}".format(self.name)

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key="true")
    title = db.Column(db.String(100), nullable=False, index=True)
    author = db.Column(db.String(100))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(100))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())
    #foreign key
    pub_id = db.Column(db.Integer, db.ForeignKey('publications.id'))

    def __init__(self, title, author, avg_rating, format, image, num_pages, pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id
    
