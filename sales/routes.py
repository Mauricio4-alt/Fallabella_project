from config import create_app,db
from flask import request,jsonify
# from models import 

app = create_app()




@app.route('/add_sale/<int:id>',methods=['POST'])
def add_sale(id):
    pass



if __name__=="__main__":
    with app.app_context():
        db.create_all()
        print('Base de datos inicializada con éxito 🎉')
    app.run(debug=True,port=5003)