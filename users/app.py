from config import app,db
from flask import request, jsonify
from models import Users

@app.route('/add_user')
def add_user():
    name = request.json['userName']
    email = request.json['email']
    password = request.json['password']
    if not name or not email or not password:
        return jsonify({'message':'Lo sentimos pero falta el name o el email o el password'})
    try:
        user = Users(name=name,email=email,password=password)
        db.session.add(user)
        db.session.commit()
    except :
        return jsonify({'message':'Sorry Internal Server Error'})