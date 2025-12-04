#The file taxi.py contains the definition of a class describing taxi rides. 
# Complete the class by adding a method print_receipt(self) that prints receipt.
#  It should contain all the information about the ride: distance, rate, and fare.
#  Then write a program in which you create two objects representing two different taxi rides. 
# Calculate the fares for the two rides and print receipts.



class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f'Your distance is {self.distance} km, rate per km is {self.rate_per_km}, fare is {self.fare}')

a= TaxiRide(4)
a.calculate_fare(5)
a.print_receipt()


