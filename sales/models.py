from datetime import datetime
from config import db
from sqlalchemy.dialects.postgresql import ARRAY 
class VentasFallabella(db.Model):
    __tablename__="VentasFallabella"
    id = db.Column(db.Integer,primary_key=True)
    customer = db.Column(db.String(255),nullable=False)
    products = db.Column(ARRAY(db.Integer),nullable=False)
    id_user= db.Column(db.Integer,nullable = False,index=True)
    total = db.Column(db.Integer,nullable=False)
    fecha = db.Column(db.Date,default=datetime.today)