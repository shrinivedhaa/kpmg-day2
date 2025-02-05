import threading
import time
import random

# Shared resource: A queue of orders
orders = ["Espresso", "Cappuccino", "Latte", "Americano", "Mocha", "Macchiato"]
order_lock = threading.Lock()

# Function for baristas to process orders
def barista(barista_name):
    while orders:
        order_lock.acquire()  # Ensure only one thread accesses the shared resource at a time
        if orders:  # Recheck after acquiring lock to avoid race conditions
            item= orders.pop(0)
            print(f"{barista_name} is preparing {item}...")
        order_lock.release()

        if item:
            time_to_prepare = random.uniform(1, 3)  # Random preparation time
            time.sleep(time_to_prepare)
            print(f"{barista_name} has completed {item} in {time_to_prepare:.2f} seconds!")
        else:
            break

# Create threads for multiple baristas
barista1 = threading.Thread(target=barista, args=("Barista Alice",))
barista2 = threading.Thread(target=barista, args=("Barista Bob",))
barista3 = threading.Thread(target=barista, args=("Barista Charlie",))

# Start threads
barista1.start()
barista2.start()
barista3.start()

# Wait for all threads to finish
barista1.join()
barista2.join()
barista3.join()

print("All orders have been processed!")
