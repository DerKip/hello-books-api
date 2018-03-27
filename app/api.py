from flask import Flask,request,jsonify,abort
from flask_api import FlaskAPI
import uuid #generates random public id
from werkzeug.security import generate_password_hash, check_password_hash
from classes import *

app=Flask(__name__)

app.config['SECRET_KEY']='siri'


@app.route('/book',methods=['POST'])
def add_a_book():
    """"""
    data=request.get_json()
    new_book=Books()
    new_book.book_id=str(uuid.uuid1())
    new_book.book_title=data['title']
    new_book.edition=data['edition']
    new_book.author=data['author']
    new_book.publisher=data['publisher']
    return jsonify(new_book.__dict__) 


@app.route('/api/books/<bookId>',methods=['PUT'])
def modify_book():
    return ''

@app.route('/api//books/<bookId>',methods=['DELETE'])
def remove_a_book():
    return ''

@app.route('/api/books/<bookId>',methods=['GET'])
def get_books():
    return ''

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
    # response.status_code = 201
    return jsonify(new_user.__dict__)


@app.route('/api/auth/login',methods=['POST'])
def login():
    return ''

@app.route('/api/auth/reset-password',methods=['POST'])
def reset_password():
    return ''

if __name__=='__main__':
    app.run(debug=True)