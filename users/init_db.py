from config import app,db
from models import Users

if __name__=='__main__':
    with app.app_context():
        db.create_all()
        print('La base de datos se creó de forma exitosa 🎉')