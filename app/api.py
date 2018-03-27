from flask import Flask,request,jsonify,abort
from flask_api import FlaskAPI
import uuid #generates random public id
from werkzeug.security import generate_password_hash, check_password_hash
from classes import *

app=Flask(__name__)

app.config['SECRET_KEY']='siri'


@app.route('/book',methods=['POST'])
def add_a_book():
    """adds a book to books"""
    data=request.get_json()
    new_book=Books()
    new_book.book_id=str(uuid.uuid1())
    new_book.book_title=data['title']
    new_book.edition=data['edition']
    new_book.author=data['author']
    new_book.publisher=data['publisher']
    book_data=new_book.__dict__
    Books.books.append(book_data)
    return jsonify(book_data) 


@app.route('/api/books/<bookId>',methods=['PUT'])
def modify_book():
    return ''

@app.route('/api//books/<bookId>',methods=['DELETE'])
def remove_a_book():
    return ''

@app.route('/api/books/',methods=['GET'])
def retrive_all_books():
    """displays all books in book list"""
    return jsonify({'books':Books.books})

@app.route('/api/books/<bookid>',methods=['GET'])
def get_a_books(bookid):
    """endpoint for finding a particular book"""
    book_searched=Books.get_book_by_id(bookid)
    return jsonify({'result':book_searched})
    
@app.route('/api/users/books/<bookId>',methods=['POST'])
def borrow_book():
    return ''

@app.route('/api/auth/register',methods=['POST'])
def create_user():
    """endpoint for creating a user"""
    data=request.get_json()
    hashed_password=generate_password_hash(data['password'],method='sha256')
    new_user=User()
    new_user.public_id=str(uuid.uuid4())
    new_user.name=data['name']
    new_user.password=hashed_password
    new_user.admin=False
    user_data=(new_user.__dict__)
    User.users.append(user_data)
    return jsonify(new_user.__dict__)


@app.route('/api/auth/login',methods=['POST'])
def login():
    return ''

@app.route('/api/auth/reset-password',methods=['POST'])
def reset_password():
    return ''

if __name__=='__main__':
    app.run(debug=True)