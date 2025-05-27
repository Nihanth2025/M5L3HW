class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def fare(self):
        fare = super().fare()
        return fare + (0.1 * fare)

o = Bus("TATA MOTORS", 50)
print(o.fare())
