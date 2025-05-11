from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PTE(db.Model):
    __tablename__ = "ptes"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

class SchoolRecord(db.Model):
    __tablename__ = "SchoolRecords"
    id = db.Column(db.Integer, primary_key=True)
    admission_no = db.Column(db.String(20), unique=True, nullable=False)
    student_name = db.Column(db.String(100))
    parent_email = db.Column(db.String(100))

class LateRecord(db.Model):
    __tablename__ = "LateRecords"
    id = db.Column(db.Integer, primary_key=True)
    admission_no = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20))
    reason = db.Column(db.Text)
