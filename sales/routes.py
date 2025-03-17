from config import create_app,db
from flask import request,jsonify
from models import VentasFallabella
# from models import 

app = create_app()




@app.route('/add_sale/<int:id>',methods=['POST'])
def add_sale(id):
    data = request.get_json()
    customer = data.get('cliente')
    products = data.get('producto')
    total = data.get('total')
    if not data or not 'cliente' in data or not 'producto' in data or not 'total' in data:
        return jsonify({'message':'Error no se han introducido correctamenter los datos'})
    try:
        venta = VentasFallabella(customer=customer,products=products,total=total,id_user=id)
        db.session.add(venta)
        db.session.commit()
        return jsonify({'message':'Venta efectuada exitosamente'})
    except Exception :
        return jsonify({'message':' internal server Error'})



if __name__=="__main__":
    with app.app_context():
        db.create_all()
        print('Base de datos inicializada con éxito 🎉')
    app.run(debug=True,host='0.0.0.0',port=5000)