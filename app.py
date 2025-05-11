from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file
from models import db, PTE, SchoolRecord, LateRecord
from utils import export_csv, create_analytics_chart
from email_utils import send_mail
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv('.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username").strip()
        password = request.form.get("password").strip()
        user = PTE.query.filter_by(username=username, password=password).first()
        if user:
            session["user_id"] = user.id
            flash("Logged in successfully!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials", "danger")
    return render_template("login.html")

@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        admission_no = request.form.get("admission_no").strip()
        reason = request.form.get("reason").strip()

        record_count = LateRecord.query.filter_by(admission_no=admission_no).count()
        if record_count < 3:
            new_record = LateRecord(admission_no=admission_no, date=str(request.form.get("date")), reason=reason)
            db.session.add(new_record)
            db.session.commit()

            student = SchoolRecord.query.filter_by(admission_no=admission_no).first()
            if student:
                subject = "Late Arrival Notification"
                body = f"Dear Parent, your child with Admission No {admission_no} was late on {new_record.date}."
                send_mail(student.parent_email, subject, body)
            flash("Late record added and email sent!", "success")
        else:
            flash("Student has exceeded allowed chances!", "warning")

    records = LateRecord.query.all()
    return render_template("dashboard.html", records=records)

@app.route('/export')
def export():
    path = export_csv(db)
    return send_file(path, as_attachment=True)

@app.route('/analytics')
def analytics():
    chart_path = create_analytics_chart(db)
    return render_template("analytics.html", chart=chart_path)

@app.route('/logout')
def logout():
    session.pop("user_id", None)
    flash("Logged out!", "info")
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
