class Ride:
    def __init__(self, race_id, driver, passenger, distance):
        self.race_id = race_id
        self.driver = driver
        self.passenger = passenger
        self.distance = distance # in kilometers
        self.status = "requested"
        self.price = 0.0

    def start_race(self):
        if not self.motorista.available:
            raise Exception("Driver unavailable")
        self.status = "in progress"
        self.driver.update_status(False)

    def finish_race(self):
        if self.status != "in progress":
            raise Exception("The race has not started yet")
        self.status = "finished"
        self.price = self.calcular_value()
        self.driver.update_status(True)

    def calculate_value(self):
        base_rate = 5.0 # Initial fixed rate
        price_per_km = 2.5 # value per kilometer
        return base_rate + (price_per_km * self.distance)

    def __repr__(self):
        return (f"Race(id = {self.id_racing}, driver = {self.driver.name}, "
                f"passenger = {self.passenger.name}, status = {self.status}, value = {self.price})")
