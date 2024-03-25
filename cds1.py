import threading
import time
import queue
import tkinter as tk

class Client:
    def __init__(self, client_id, dispatcher):
        self.id = client_id
        self.dispatcher = dispatcher

    def request_ride(self, pickup_location, destination):
        print(f"Client {self.id} requests a ride from {pickup_location} to {destination}")
        RideRequest(self.id, pickup_location, destination).submit(self.dispatcher)  

class RideRequest:
    def __init__(self, client_id, pickup_location, destination):
        self.client_id = client_id
        self.pickup_location = pickup_location
        self.destination = destination

    def submit(self, dispatcher):
        dispatcher.request_queue.put(self)

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

class TaxiServiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxi Service App")

        self.client_frame = tk.Frame(self.root)
        self.client_frame.pack(padx=10, pady=10)

        self.pickup_label = tk.Label(self.client_frame, text="Pickup Location:")
        self.pickup_label.grid(row=0, column=0)
        self.pickup_entry = tk.Entry(self.client_frame)
        self.pickup_entry.grid(row=0, column=1)

        self.destination_label = tk.Label(self.client_frame, text="Destination:")
        self.destination_label.grid(row=1, column=0)
        self.destination_entry = tk.Entry(self.client_frame)
        self.destination_entry.grid(row=1, column=1)

        self.request_button = tk.Button(self.client_frame, text="Request Ride", command=self.request_ride)
        self.request_button.grid(row=2, columnspan=2)

    def request_ride(self):
        pickup_location = self.pickup_entry.get()
        destination = self.destination_entry.get()
        client_id = len(clients) + 1
        client = Client(client_id, dispatcher)
        client.request_ride(pickup_location, destination)

# Setup
root = tk.Tk()
app = TaxiServiceApp(root)

dispatcher = Dispatcher()
drivers = [TaxiDriver(i) for i in range(1, 4)]  # Create some drivers
for driver in drivers:
    dispatcher.register_driver(driver)

dispatch_thread = threading.Thread(target=dispatcher.dispatch)
dispatch_thread.start()

# Client requests
clients = [Client(i, dispatcher) for i in range(1, 6)]

root.mainloop()
