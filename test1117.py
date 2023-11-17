import threading
import queue
import time
import random

class Order:
    def __init__(self, id, process_time):
        self.id = id
        self.process_time = process_time

class Processor(threading.Thread):
    def __init__(self, id, order_queue):
        threading.Thread.__init__(self)
        self.id = id
        self.order_queue = order_queue
        self.orders_processed = 0
        self.total_process_time = 0

    def run(self):
        while not self.order_queue.empty():
            order = self.order_queue.get()
            start_time = time.time()
            # Simulate order processing time
            time.sleep(order.process_time)
            end_time = time.time()
            elapsed_time = end_time - start_time
            self.orders_processed += 1
            self.total_process_time += elapsed_time
            print(f"Processor {self.id} completed Order {order.id} in {elapsed_time} seconds")
        print(f"Processor {self.id} completed {self.orders_processed} orders. Average processing time: {self.total_process_time/self.orders_processed if self.orders_processed != 0 else 0}")

def simulate_restaurant_orders(num_orders, max_order_process_time, num_processors):
    # Create orders
    orders = queue.Queue()
    for i in range(num_orders):
        orders.put(Order(i, random.uniform(0.1, max_order_process_time)))

    # Create processors
    processors = [Processor(i, orders) for i in range(num_processors)]

    # Start all processors
    for processor in processors:
        processor.start()

    # Wait for all processors to finish
    for processor in processors:
        processor.join()

if __name__ == "__main__":
    num_orders = int(input("Enter the number of orders to simulate: "))
    max_processing_time = int(input("Enter the maximum time to complete processing a single order: "))
    num_processors = int(input("Enter the number of simultaneous order processors: "))
    simulate_restaurant_orders(num_orders, max_processing_time, num_processors)
