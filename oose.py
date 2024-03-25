from collections import defaultdict

class MessageDispatcher:
    def __init__(self):
        self.channels = defaultdict(list)

    def add_receiver(self, channel, receiver):
        self.channels[channel].append(receiver)

    def remove_receiver(self, channel, receiver):
        if receiver in self.channels[channel]:
            self.channels[channel].remove(receiver)

    def dispatch_message(self, channel, message):
        if channel in self.channels:
            for receiver in self.channels[channel]:
                receiver.receive_message(message)

class Client:
    def __init__(self, name):
        self.name = name

    def send_message(self, dispatcher, channel, message):
        print(f"{self.name} sends message: {message} to channel {channel}")
        dispatcher.dispatch_message(channel, message)

class Receiver:
    def __init__(self, name):
        self.name = name

    def receive_message(self, message):
        print(f"{self.name} received message: {message}")


# Example usage:
dispatcher = MessageDispatcher()

# Creating receivers for different channels
receiver1 = Receiver("Receiver1")
receiver2 = Receiver("Receiver2")

# Adding receivers to specific channels
dispatcher.add_receiver("channel1", receiver1)
dispatcher.add_receiver("channel2", receiver2)

# Creating clients
client1 = Client("Client1")
client2 = Client("Client2")

# Clients sending messages to different channels
client1.send_message(dispatcher, "channel1", "Hello from Client1")
client2.send_message(dispatcher, "channel2", "Hello from Client2")
