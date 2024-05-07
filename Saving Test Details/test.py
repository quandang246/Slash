# test.py

import slash

class Car:
    def __init__(self, model, mileage):
        self.model = model
        self.mileage = mileage

    def get_mileage(self):
        return self.mileage

    def is_van(self):
        return self.model == 'van'

# Define test cases
@slash.fixture
def car():
    return Car('sedan', 5000)  # Creating a car instance for testing

def test_steering_wheel(car):
    mileage = car.get_mileage()
    slash.context.result.details.set('mileage', mileage)

def test_car_type(car):
    is_van = car.is_van()
    slash.context.result.facts.set('is_van', is_van)
