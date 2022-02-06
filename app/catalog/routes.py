from app.catalog import main
from app import db
from app.catalog import models
from app.catalog.models import Book, Publications
from flask import render_template


@main.route('/')
def display_books():
    books = Book.query.all()
    return render_template('home.html', books=books)

@main.route('/display/publisher/<publisher_id>')
def display_publisher(publisher_id):
    pub_id = Publications.query.filter_by(id=publisher_id).first()
    publisher_books = Book.query.filter_by(pub_id=pub_id.id).all()
    return render_template('publisher.html', publisher=pub_id, publisher_books=publisher_books)