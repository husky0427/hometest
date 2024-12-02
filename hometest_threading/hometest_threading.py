import random
import threading
import time

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 999
CONSUMER_DELAY = 0.15
PRODUCER_DELAY = 0.1
MAX_SIZE_OF_QUEUE = 10


class Queue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.lock = threading.Lock()
        self.queue = []

    def put(self, number):
        with self.lock:
            if len(self.queue) < self.maxsize:
                self.queue.append(number)
                print(f"Number {number} added to queue")
            else:
                print("Queue is full")

    def get(self):
        with self.lock:
            if len(self.queue) > 0:
                number = self.queue.pop(0)
                print(f"Number {number} removed from queue")
            else:
                print("Queue is empty")

    def is_full(self):
        with self.lock:
            return len(self.queue) == self.maxsize

    def is_empty(self):
        with self.lock:
            return len(self.queue) == 0


def generate_random_number():
    random_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    return random_number


def producer(queue):
    while True:
        number = generate_random_number()
        if queue.is_full():
            print("Queue is full")
            time.sleep(PRODUCER_DELAY)
        queue.put(number)
        time.sleep(PRODUCER_DELAY)


def consumer(queue):
    while True:
        if queue.is_empty():
            print("Queue is empty")
            time.sleep(CONSUMER_DELAY)
        queue.get()
        time.sleep(CONSUMER_DELAY)


q = Queue(maxsize=MAX_SIZE_OF_QUEUE)


def run():
    producer_thread = threading.Thread(target=producer, args=(q,))
    consumer_thread = threading.Thread(target=consumer, args=(q,))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()


if __name__ == "__main__":
    run()
