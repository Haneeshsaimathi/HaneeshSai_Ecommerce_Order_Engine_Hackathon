from datetime import datetime

logs = []

def log(msg):
    entry = f"[{datetime.now()}] {msg}"
    logs.append(entry)

def view_logs():
    for l in logs:
        print(l)
