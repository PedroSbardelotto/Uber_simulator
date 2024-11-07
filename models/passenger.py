class Passenger:
    def __init__(self, name, destination, departure_location):
        self.name = name
        self.destination = destination
        self.departure_location = departure_location
         
    def update_destinations(self, new_destination):
        self.destination = new_destination

    def __repr__(self):
        return f"Passenger(name = {self.name}, departure = {self.departure_location}, destination = {self.destination})"
