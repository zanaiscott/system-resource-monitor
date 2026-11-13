import csv
import os
from datetime import datetime

PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))
LOG_FOLDER = os.path.join(PROJECT_FOLDER, "logs")
LOG_FILE = os.path.join(LOG_FOLDER, "snapshots.csv")
FIELDNAMES = ["timestamp", "cpu_percent", "memory_percent", "memory_used_gb", "memory_total_gb", "disk_percent", "disk_used_gb", "disk_total_gb"]

def get_timestamp():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")
def needs_header():
    if not os.path.exists(LOG_FILE):
        return True
    if os.path.getsize(LOG_FILE) == 0:
        return True
    return False

def save_snapshot(summary):
    os.makedirs(LOG_FOLDER, exist_ok=True)
    write_header = needs_header()
    row = {
        "timestamp": get_timestamp(),
        "cpu_percent": summary["cpu_percent"],
        "memory_percent": summary["memory_percent"],
        "memory_used_gb": summary["memory_used_gb"],
        "memory_total_gb": summary["memory_total_gb"],
        "disk_percent": summary["disk_percent"],
        "disk_used_gb": summary["disk_used_gb"],
        "disk_total_gb": summary["disk_total_gb"],
    }
    with open(LOG_FILE, mode="a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerow(row)
        return row
    