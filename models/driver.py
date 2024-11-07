class Driver:
    def __init__(self, name, vehicle, available=True):
        self.name = name
        self.vehicle = vehicle
        self.available = available

    def update_status(self,available):
        self.available = available

    def to_dict(self):
        return {
            "name": self.name,
            "vehicle": self.vehicle,
            "available": self.available,
        }
    