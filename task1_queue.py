from queue import Queue
import random
import time

queue = Queue()

def generate_request():
    request_id = f"Request_{random.randint(100, 999)}"
    queue.put(request_id)
    print(f"Додано заявку: {request_id}")

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Обробляється заявка: {request}")
        time.sleep(1)  # Імітація часу обробки
    else:
        print("Черга порожня")

while True:
    for _ in range(random.randint(1, 2)):
        generate_request()
    
    for _ in range(random.randint(1, 2)):
        process_request()
    
    print(f"Розмір черги: {queue.qsize()}")
    time.sleep(2)