from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify
from time import sleep
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:asd123asd@localhost:5432/ostimApp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db = SQLAlchemy(app)


def add_usera():
    user = Users(companyName="SAFA KULLANICIK",
                 companyAddress="bizim evin oralar ehue heue",
                 mail="safa1@safa.com",
                 passwd=generate_password_hash("asd123"),
                 isAdmin=False,
                 taxNo="1234567890",
                 telNo="12332112331")
    db.session.add(user)
    db.session.commit()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.String(80))
    companyAddress = db.Column(db.String(250))
    mail = db.Column(db.String(40), unique=True)
    passwd = db.Column(db.String(128))
    isAdmin = db.Column(db.BOOLEAN)
    taxNo = db.Column(db.String(10))
    telNo = db.Column(db.String(11))

    applies = db.relationship('Apply', backref='users')


class Apply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    authNameSurname = db.Column(db.String(50))
    authTc = db.Column(db.Numeric(11, 0))
    authTelNo = db.Column(db.Numeric(10, 0))
    authVehiclePlaque = db.Column(db.String(10))
    duty = db.Column(db.String(50))
    gotIndustryRecord = db.Column(db.BOOLEAN)
    industryRecordNo = db.Column(db.String(50))
    relatedEntry = db.Column(db.String(50))
    editDate = db.Column(db.DATE)
    startDate = db.Column(db.DATE)
    endDate = db.Column(db.DATE)
    isNew = db.Column(db.BOOLEAN)
    isEnd = db.Column(db.BOOLEAN)
    isapproved = db.Column(db.BOOLEAN)

    userId = db.Column(db.Integer, db.ForeignKey('users.id'))

    staff = db.relationship('Staff_Info', backref='apply')


class Staff_Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staffNameSurname = db.Column(db.String(50))
    staffDuty = db.Column(db.String(50))
    vehiclePlaque = db.Column(db.String(10))
    staffTc = db.Column(db.Numeric(11, 0))

    applyId = db.Column(db.Integer, db.ForeignKey('apply.id'))


@app.route('/api/checkUser', methods=["GET", "POST"])
def check_user():
    user = Users.query.filter_by(mail=request.json["mail"]).first()
    if user is None:
        return jsonify(result="2", data="Böyle Bir Kullanıcı Yok.")
    if check_password_hash(user.passwd, request.json["passwd"]):
        output = user.__dict__
        del output["passwd"]
        del output["_sa_instance_state"]
        print(output)
        return jsonify(result="0", data=output)
    else:
        return jsonify(result="1", data="Hatalı Şifre Girildi.")


@app.route('/api/getUsers', methods=["GET"])
def get_users():
    users = Users.query.all()
    if users is None:
        return jsonify(result=[])
    output = []
    for i, user in enumerate(users):
        temp = {}
        temp = user.__dict__
        del temp["passwd"]
        del temp["_sa_instance_state"]
        temp["index"] = i+1
        output.append(temp)
    return jsonify(result=output)


@app.route('/api/addUser', methods=["POST"])
def add_user():
    user = request.json["user"]
    new = Users(companyName=user["companyName"],
                companyAddress=user["companyAddress"],
                mail=user["mail"],
                passwd=generate_password_hash(user["passwd"]),
                isAdmin=bool(user["isAdmin"]),
                taxNo=user["taxNo"],
                telNo=user["telNo"])
    db.session.add(new)
    db.session.commit()
    return jsonify(result=True)


@app.route('/api/getAllApplies', methods=["POST"])
def get_all_applies():
    if request.json["isAdmin"]:
        applies = Apply.query.all()
    else:
        applies = Apply.query.filter_by(userId=request.json["id"]).all()
    if applies is None:
        return jsonify(result=[])
    output = []
    for i, apply in enumerate(applies):
        #user = Users.query.filter_by(id=apply.userId).first()
        temp = {}
        temp = apply.__dict__
        del temp["_sa_instance_state"]
        temp["index"] = i+1
 
        output.append(temp)
    return jsonify(result=output)


@app.route('/api/delUser', methods=["POST"])
def del_user():
    Users.query.filter_by(id=request.json["id"]).delete()
    db.session.commit()
    return jsonify(result=True)


@app.route("/api/test", methods=["GET"])
def yaz():
    sleep(2)
    return jsonify(result=veri)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
