from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sbms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class SBMS(db.Model):
    rollno=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200), nullable=False)
    fname=db.Column(db.String(200), nullable=False)
    mname=db.Column(db.String(200), nullable=False)
    gender=db.Column(db.String(20), nullable=False)
    dob=db.Column(db.String(200), nullable=False)
    course=db.Column(db.String(100), nullable=False)
    branch=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(200), nullable=False)
    phone=db.Column(db.String(15), nullable=False)
    gradyear=db.Column(db.Integer, nullable=False)
    add=db.Column(db.String(500), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self)->str:
        return f"{self.rollno} - {self.name}"

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        rollno = request.form["roll"]
        name = request.form["name"]
        fname = request.form["fname"]
        mname = request.form["mname"]
        gender = request.form["gender"]
        dob = request.form["dob"]
        course = request.form["course"]
        branch = request.form["branch"]
        email = request.form["email"]
        phone = request.form["phone"]
        gradyear = request.form["gradyear"]
        add = request.form["add"]
        sbms = SBMS(rollno=rollno, name=name,fname=fname, mname=mname, gender=gender, dob=dob, course=course, branch=branch, email=email, phone=phone, gradyear=gradyear,  add=add)
        db.session.add(sbms)
        db.session.commit()

    allSBMS = SBMS.query.all()
    return render_template('index.html', allSBMS=allSBMS)


@app.route("/show")
def products():
    allSBMS=SBMS.query.all()
    print(allSBMS)
    return("this is prodcuts page")

@app.route("/update/<int:rollno>", methods=['GET', 'POST'])
def update(rollno):
    if request.method=='POST':
        rollno = request.form["roll"]
        name = request.form["name"]
        fname = request.form["fname"]
        mname = request.form["mname"]
        gender = request.form["gender"]
        dob = request.form["dob"]
        course = request.form["course"]
        branch = request.form["branch"]
        email = request.form["email"]
        phone = request.form["phone"]
        gradyear = request.form["gradyear"]
        add = request.form["add"]
        sbms=SBMS.query.filter_by(rollno=rollno).first()
        sbms.rollno=rollno
        sbms.name=name
        sbms.fname=fname
        sbms.mname=mname
        sbms.gendergender=name
        sbms.dob=dob
        sbms.course=course
        sbms.branch=branch
        sbms.email=email
        sbms.phone=phone
        sbms.gradyear=gradyear
        sbms.add=add
        db.session.add(sbms)
        db.session.commit()
        return redirect("/")

    sbms=SBMS.query.filter_by(rollno=rollno).first()
    return render_template('update.html', sbms=sbms)

@app.route("/delete/<int:rollno>")
def delete(rollno):
    sbms=SBMS.query.filter_by(rollno=rollno).first()
    db.session.delete(sbms) 
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)

