from config import db

class TradeBrands(db.Model):
    __tablename__ = 'TradeBrands'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    
    # Relación con Products (un TradeBrand puede tener muchos Products)
    products = db.relationship('Products', backref='trade_brand', lazy=True)


class Products(db.Model):
    __tablename__ = 'Products'
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(250), unique=True, nullable=False)
    price = db.Column(db.Integer)

    # Relación con TradeBrands
    tradeBrand = db.Column(db.Integer, db.ForeignKey('TradeBrands.id'), nullable=False)

    # Referencia externa a un usuario en otro servicio
    id_user = db.Column(db.Integer, nullable=False, index=True)
