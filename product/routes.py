from config import create_app ,db
from flask import request, jsonify
from models import TradeBrands,Products
app = create_app()


@app.route('<int:id>/add_brand',methods=['POST'])
def add_brand(id):
    
    name = request.json['brand']
    if not name  :
        return jsonify({'message':'debe ingresar el nombre de una marca'})
    try:
        brand = TradeBrands(name=name)
        db.session.add(brand)
        db.session.commit()
        return jsonify ({'message':'nueva marca registrada'})
    except Exception as e:
        print(f'e: {e}')
        return jsonify({'message':'Sorry internal server error'})
    
    
    
@app.route('<int:id>/add_product',methods=['POST'])
def add_product(id):
    data = request.get_json()
    product = data['product']
    price = data['price']
    tradeBrand = data['brand']
    idUser = id
    if not data or  not 'product' in data or not 'price' in data or not 'brand' in data:
        return jsonify({'message':'lo sentimos faltan datos'})
    try:
        tradeBrand = TradeBrands.query.filter_by(name=tradeBrand).first()
        product = Products( product=product,price=price,tradeBrand=tradeBrand.id,id_user=idUser)
        db.session.add(product)
        db.session.commit()
        return jsonify({'message':'Se ha insertado un nuevo producto'})
    except Exception as e:
        print(f'e: {e}')
        return jsonify({'message':'Sorry internal server error'})





if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,host='0.0.0.0',port=5002)