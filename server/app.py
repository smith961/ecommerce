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

@app.route("/adminRegister", methods = ['POST'])
def adminRegister():
    allusers = User.query.all()
    # allusers = mongo.db.admins

    # user = allusers.find_one({'email': request.json['email']})
    # companyName = allusers.find_one({'companyName': request.json['companyName']})
    # phone = allusers.find_one({'phone': request.json['phone']})
    user = User(
        email = request.form.get("email"),
        companyName = request.form.get("companyName"),
        phone = request.form.get("phone")
    )
    db.session.add(user)
    db.session.commit()
    # if user:
    #     return jsonify(message='Email already exists'), 401
    # if companyName:
    #     return jsonify(message='companyName already exists'), 401
    # if phone:
    #     return jsonify(message='Phone Number already exists'), 401
    
    # if request.json['password'] != request.json['cpassword']:
    #     return jsonify(message='Password not Matching!!!'), 401
    user_dict = user.to_dict()
    response = make_response(user_dict, 201)
    return response

@app.route("/adminLogin", methods=['POST'])
def adminLogin():
    allusers = User.query.all()

@app.route("/logoutAdmin", methods = ['POST'])
def logoutAdmin():
    pass   

if __name__ == '__main__':
    app.run(debug=True)






