from config import create_app ,db
from flask import request, jsonify
from models import Users
app = create_app()


@app.route('/add_user',methods=['POST'])
def add_user():
    data = request.get_json()
    name = data['userName']
    email = data['email']
    password = data['password']
    if  not data or  'userName' not in data or 'email' not in data or 'password' not in data :
        return jsonify({'message':'faltan datos'}),400
    try:
        user = Users(name=name,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message":"usuario creado exitosamente"}),201
    except Exception as err :
        print(err)
        db.session.rollback()
        return jsonify({'message':'Sorry Internal Server Error'}),500
@app.route('/get_user',methods=['POST'])
def get_user():
    data = request.get_json()
    email = data['email']
    password =data['password']
    if not data or not 'email' in data or not 'password' in data:
        return jsonify({'message':'Credenciales incorrectas'})
    try:
        user= Users.query.filter_by(email=email,password=password).first()
        return jsonify({'user_info':{'id':user.id,'userName':user.name}})

    except Exception as e:
        print(f'Error {e}')
        return jsonify({'message':'Sorry internal server error'})
@app.route('/update_user/<int:id>',methods=['PATCH'])
def update_user(id):
    data = request.get_json()
    try:
        user= Users.query.filter_by(id=id).first()
        if 'password' in data:
            user.password = data['password']
            db.session.commit()
        if 'email' in data:
            user.email = data['email']
            db.session.commit()
        if 'email' in data:
            user.name = data['userName']
            db.session.commit()


        return jsonify({'user_info':{'userName':user.name,'password':user.password,'email':user.email}})
    except Exception as e:
        print(f'Error {e}')
        return jsonify({'message':'Sorry internal server error'})
@app.route('/delete_user/<int:id>',methods=['DELETE'])
def delete_user(id):
    
    try:
        user= Users.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message':'User deleted succesfull'})

    except Exception as e:
        print(f'Error {e}')
        return jsonify({'message':'User not found'})
    

         
    




if __name__=='__main__':
    with app.app_context():
        db.create_all()
        print('Conexion creada de forma exitosa 🎉')
    app.run(debug=True,host='0.0.0.0',port=5000)