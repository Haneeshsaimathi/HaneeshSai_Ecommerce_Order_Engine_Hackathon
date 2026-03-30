events = []

def push_event(event):
    events.append(event)

def process_events():
    while events:
        e = events.pop(0)
        print("Processing:", e)
