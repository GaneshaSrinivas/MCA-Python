from abc import *
class Vehicle(ABC): 

    def __init__(self, typ, make, model, color, year, miles):
        self.typ = typ
        self.make = make
        self.model = model
        self.color = color.lower()
        self.year = year
        self.miles = miles
    @abstractmethod
    def vehicle_print(self):
          pass


class FuelVehicle(Vehicle):

    def __init__(self, fuel_tank, *args):
        self.fuel_tank = fuel_tank
        Vehicle.__init__(self, *args)

    def vehicle_print(self):
        Vehicle.vehicle_print(self)
        print('Vehicle Type: ' + str(self.typ))
        print('Make: ' + str(self.make))
        print('Model: ' + str(self.model))
        print('Color: ' + str(self.color))
        print('Year: ' + str(self.year))
        print('Miles driven: ' + str(self.miles))
        print('Fuel capacity (L): ' + str(self.fuel_tank))
   


class ElectricVehicle(Vehicle):

    def __init__(self, energy_storage, *args):
        self.energy_storage = energy_storage
        Vehicle.__init__(self, *args)

    def vehicle_print(self):
        Vehicle.vehicle_print(self)
        print('Vehicle Type: ' + str(self.typ))
        print('Make: ' + str(self.make))
        print('Model: ' + str(self.model))
        print('Color: ' + str(self.color))
        print('Year: ' + str(self.year))
        print('Miles driven: ' + str(self.miles))
        print('Energy Storage (Kwh): ' + str(self.energy_storage))


bmw = FuelVehicle(80, 'SUV', 'BMW', 'X5', 'silver', 2003, 120300)  # regular car
bmw.vehicle_print()
print("-----------------------------------------\n")
tesla = ElectricVehicle(85, 'Sport', 'Tesla', 'Model S', 'red', 2014, 1243)  # electric car
tesla.vehicle_print()
