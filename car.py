import random
from speed import Speed


class Car:
    def __init__(self, make, age, color, speed):
        self.make = make
        self.age = age
        self.color = color
        self.speed = Speed.velocity(0)

    def drive(self):
        print(f"{self.color} {self.make} is going fast at speed {self.speed}")


make = ['Audi', 'BMW', 'Volvo', 'Toyota']
age = [5, 6, 12, 20]
colors = ['blue', 'black', 'purple', 'red']

cars = []
for x in range(len(make)):

    b = random.randint(0,3)
    c = random.randint(0,3)
    car = Car(make[x], age[b], colors[c], Speed)
    cars.append(car)

for t in range(len(cars)):

    cars[t].drive()





