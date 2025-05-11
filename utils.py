import os
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from models import LateRecord

def export_csv(db):
    records = LateRecord.query.all()
    export_folder = os.path.join(os.getcwd(), "exported_data")
    os.makedirs(export_folder, exist_ok=True)
    path = os.path.join(export_folder, "late_records.csv")
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Admission No", "Date", "Reason"])
        for record in records:
            writer.writerow([record.id, record.admission_no, record.date, record.reason])
    return path

def create_analytics_chart(db):
    records = LateRecord.query.all()
    data = {}
    for record in records:
        data[record.admission_no] = data.get(record.admission_no, 0) + 1

    labels = list(data.keys())
    values = list(data.values())

    chart_folder = os.path.join(os.getcwd(), "static", "charts")
    os.makedirs(chart_folder, exist_ok=True)
    chart_path = os.path.join(chart_folder, "analytics.png")

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color='skyblue')
    plt.xlabel("Admission No")
    plt.ylabel("Times Late")
    plt.title("Late Arrival Analytics")
    plt.savefig(chart_path)
    plt.close()

    return "charts/analytics.png"
