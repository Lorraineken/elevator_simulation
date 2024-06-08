import time
from threading import Thread
from building import Building

# Example usage of the classes defined above
if __name__ == "__main__":
    building = Building()  # building instance

    # Simulating multiple elevator requests
    requests = [3, 5, 2, 1, 4, 5, 1, 2, 2, 1, 5, 4, 3, 4]

    threads = []  # List to keep track of threads

    for floor in requests:
        # Create a new thread for each request to simulate concurrent requests
        t = Thread(target=building.request_elevator, args=(floor,))
        threads.append(t)  # Add thread to the list
        t.start()  # Start the thread

    # Join all threads to ensure completion before exiting
    for t in threads:
        t.join()  # Wait for each thread to finish




