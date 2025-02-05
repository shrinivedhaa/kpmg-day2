import threading
import time

def worker():
    print("Worker thread starting...")
    time.sleep(5)
    print("Worker thread finished...")

# Create thread
t=threading.Thread(target=worker)
t.start()

# Wait for a maximum of 2 seconds
t.join(timeout=10)

print("Main threads resumes after waiting for 2 seconds (even if worker isn't finished).")