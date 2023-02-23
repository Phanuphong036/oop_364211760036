"""
Student Name:{Phanuphong Sutthiphibun}
ID:{364211760036}
Group: {MIT222}
"""

class EV_Car:
    def __init__(self, brand, model, motor, horse_power, battery_size, range, price):
        self.brand = brand
        self.model = model
        self.motor = motor
        self.horse_power = horse_power
        self.battery_size = battery_size
        self.range = range
        self.price = price
    def EV_Car(self):
        print(f'Brand: {self.brand} Model: {self.model} motor: {self.motor} horse_power: {self.horse_power} battery_size: {self.battery_size} range: {self.range} price: {self.price}')

p1 = []
# create object EV_Car
m1 = EV_Car('Toyota','bZ4X', 1, 218, 71.6, 460, 499000)
p1.append(m1)

m2 = EV_Car ('MG', 'ZS.EV', 1, 177, 50.3, 403, 949000)
p1.append(m2)

m3 = EV_Car('Mercedes', 'EQS', 2, 333, 107.8, 770, 8570000)
p1.append(m3)

for x in p1:
    print(x.EV_Car())