from config import create_app ,db
from flask import request, jsonify
from models import TradeBrands,Products
app = create_app()


@app.route('/add_brand',methods=['POST'])
def add_brand():
    
    name = request.json['brand']
    if  not name  :
        return jsonify({'message':'debe ingresar el nombre de una marca'}),404
    try:
        brand = TradeBrands(name=name)
        db.session.add(brand)
        db.session.commit()
        return jsonify ({'message':'nueva marca registrada'}),200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message':'Sorry internal server error'}),500
    
# @app.route('/get_products/<int:id>',methods=['POST'])
# def get_products(id):
#     try:
#         products = Products.query.filter_by(id_user=id).all()
        
#         return jsonify({'products':[{'id':product.id,'product':product.product,'price':product.price }for product in products]})
#     except Exception as e:
#         return jsonify({'message':'Internal Server Error'})
    
@app.route('/add_product/<int:id>', methods=['POST'])
def add_product(id):
    data = request.get_json()
    product = data.get('product')
    price = data.get('price')
    brand_name = data.get('tradeBrand')
    
    if not product or not price or not brand_name:
        return jsonify({'message': 'Lo sentimos, faltan datos'}), 400

    try:
        tradeBrand = TradeBrands.query.filter_by(name=brand_name).first()
        if not tradeBrand:
            return jsonify({'message': 'La marca especificada no existe'}), 404
        
        new_product = Products(product=product, price=price, tradeBrand=tradeBrand.id, id_user=id)
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Se ha insertado un nuevo producto'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Sorry, internal server error'}), 500



@app.route('/update_product/<int:id>',methods=['POST'])
def update_product(id):
    data = request.get_json()
    n_product = data.get('product')
    price =data.get('price')
    tradeBrand = data.get('tradeBrand')
    if not data :
        return jsonify ({'message':'Error no se ha introducido ningún dato'})
    try:
        product = Products.query.filter_by(product =n_product,id_user =id).first()
        if price:
            product.price = price
            db.session.commit()
        if tradeBrand:
            product.tradeBrand = tradeBrand
            db.session.commit()
        return jsonify({'message':'actualizacion realizada correctamente'})
    except Exception as e:
        print(e)
        return jsonify({'message':'error internal server error'})   
    

@app.route('/delete_product/<int:id>',methods=['DELETE'])
def delete_product(id):
    data = request.get_json().get('product')
    if not data:
        return jsonify({'message':'error producto no especificado'})
    try:
        product = Products.query.filter_by(product=data,id_user=id).first()
        db.session.delete(product)
        db.session.commit()
        return jsonify ({'message':'Producto Eliminado con exito'})
    except Exception:
        return jsonify({'message':'error internal server error'})
    
if __name__=='__main__':
    with app.app_context():
        db.create_all()
        print('base de datos inicializada con éxito'
        '')
    app.run(debug=True,host='0.0.0.0',port=5000)