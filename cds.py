import threading
import time
import queue

class Client:
    def __init__(self, client_id):
        self.id = client_id

    def request_ride(self, pickup_location, destination):
        print(f"Client {self.id} requests a ride from {pickup_location} to {destination}")
        RideRequest(self.id, pickup_location, destination).submit()  

class RideRequest:
    def __init__(self, client_id, pickup_location, destination):
        self.client_id = client_id
        self.pickup_location = pickup_location
        self.destination = destination

    def submit(self):
        Dispatcher.request_queue.put(self)

class TaxiDriver:
    def __init__(self, driver_id):
        self.id = driver_id
        self.available = True

    def accept_request(self, request):
        self.available = False
        print(f"Driver {self.id} accepts ride request from Client {request.client_id}")
        # Simulate ride duration
        time.sleep(5)  
        print(f"Driver {self.id} completed the ride for Client {request.client_id}")
        self.available = True

class Dispatcher:
    request_queue = queue.Queue()
    available_drivers = []

    def register_driver(self, driver):
        self.available_drivers.append(driver)

    def dispatch(self):
        while True:
            request = self.request_queue.get()  # Wait for ride requests
            self.assign_request(request)

    def assign_request(self, request):
        for driver in self.available_drivers:
            if driver.available:
                driver.accept_request(request)
                return  # Driver assigned

# Setup
dispatcher = Dispatcher()
drivers = [TaxiDriver(i) for i in range(1, 4)]  # Create some drivers
for driver in drivers:
    dispatcher.register_driver(driver)

dispatch_thread = threading.Thread(target=dispatcher.dispatch)
dispatch_thread.start()

# Client requests
clients = [Client(i) for i in range(1, 6)]
clients[0].request_ride("Point A", "Point B")
clients[2].request_ride("Market Street", "Airport")
# ... more client requests
