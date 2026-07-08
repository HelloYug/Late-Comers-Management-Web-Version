# 🎯 Late Comers Management System - Web Application

A modern web-based system to track, manage, and analyze late arrivals of students in schools.

Built using 🐍 Flask (Python web framework), 🛢️ MySQL, 🎨 Bootstrap frontend, and 📧 SMTP for email notifications.

---

## ✨ Features

- 🔒 Secure login system for Physical Training Educators (PTEs)
- 📝 Add late-comer entries with reasons
- 📬 Automatic email notifications to parents
- ⚡ 3-Strike rule enforcement
- 📁 Export all records to CSV file
- 📊 Analytics dashboard with bar graphs
- 📱 Responsive design using Bootstrap

---

## 🛠️ Technologies Used

- Backend: Python, Flask
- Frontend: HTML, Bootstrap 5
- Database: MySQL with SQLAlchemy ORM
- Email Integration: Gmail SMTP server
- Visualization: Matplotlib
- Environment Config: Python Dotenv
- Migrations: Flask-Migrate

---

## 🗂️ Folder Structure

```
WebApp/
├── app.py               # Main Flask application
├── models.py            # Database models (PTEs, Students, Late Records)
├── email_utils.py       # Email sending functions
├── utils.py             # Export CSV and create analytics chart
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
├── README.md            # Project documentation
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── analytics.html
│   ├── index.html
├── static/
│   ├── css/
│   │   └── bootstrap.min.css
│   ├── js/
│   │   └── bootstrap.bundle.min.js
│   └── charts/          # Analytics chart images
└── exported_data/       # CSV export files
```

---

## ⚙️ Setup Instructions

1. 📥 Clone or Download the project folder.

2. 📦 Install Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. 🛡️ Configure environment variables:
   - Copy `.env.example` to `.env`
   - Fill your MySQL database URL, Flask secret key, and Gmail SMTP credentials inside `.env`

4. 🏗️ Set up MySQL Database:
   - Create a database named `LateComersDB`
   - Create the required tables: `SchoolRecords`, `LateRecords`, `PTEs`
   - (You can use SQL scripts or create manually)

5. 🛠️ Run Database Migrations:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

6. 🚀 Run the Flask Application:
   ```bash
   python app.py
   ```

7. 🌐 Open your browser and go to:
   ```
   http://localhost:5000/
   ```

---

## 🗄️ Database Tables

**Table: PTEs**
- id (Primary Key)
- username (Unique)
- password

**Table: SchoolRecords**
- id (Primary Key)
- admission_no (Unique)
- student_name
- parent_email

**Table: LateRecords**
- id (Primary Key)
- admission_no
- date
- reason

---

## 🔁 Functional Workflow

1. 🛡️ PTE logs in securely.
2. 📝 Admission number and reason for lateness is entered.
3. ⚡ If within 3 warnings, record is saved and email sent to parent.
4. 📁 Late records can be exported into a CSV.
5. 📊 Analytics page shows a bar graph of late students.

---

## 👨‍💻 Author

**Yug Agarwal**

* 📧 Email – [yugagarwal704@gmail.com](mailto:yugagarwal704@gmail.com)
* 🔗 GitHub – [@HelloYug](https://github.com/HelloYug)
* 💼 LinkedIn – [yugagarwal704](https://www.linkedin.com/in/yugagarwal704/)
* 🌐 Portfolio – [yugagarwal.dev](https://yugagarwal.dev/?utm_source=github&utm_medium=readme&utm_campaign=Late-Comers-Management-Web-Version_readme)

