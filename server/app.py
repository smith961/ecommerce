from flask import Flask, request, jsonify, make_response;
from flask_sqlalchemy import SQLAlchemy;
from flask_cors import CORS;
from flask_migrate import Migrate;

from models import db, User

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)


@app.route("/")
def hello_world():
    return 'Hello world'

@app.route("/adminRegister", methods = ['GET','POST'])
def adminRegister():
    if request.method == 'GET':
        return make_response(
            [user.to_dict() for user in User.query.all],
            200
        )
    elif request.method == 'POST':
         user = User(
        email = request.form.get("email"),
        companyName = request.form.get("companyName"),
        phone = request.form.get("phone")
    )
         db.session.add(user)
         db.session.commit()
    
    user_dict = user.to_dict()
    response = make_response(user_dict, 201)
    return response

@app.route("/adminLogin", methods=['GET','POST'])
def adminLogin():
    if request.method == 'GET':
        return make_response(
            [user.to_dict() for user in User.query.all()],
            200
        )
    elif request.method == "POST":
        pass
   

@app.route("/logoutAdmin", methods = ['POST'])
def logoutAdmin():
    pass   

if __name__ == '__main__':
    app.run(debug=True)






