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
    
if __name__=='__main__':
    with app.app_context():
        db.create_all()
        print('Conexion creada de forma exitosa 🎉')
    app.run(debug=True,host='0.0.0.0',port=5000)