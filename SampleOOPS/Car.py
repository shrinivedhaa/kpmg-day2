class Car:
    def __init__(self, brand, model, year):
        self.brand=brand
        self.model=model
        self.year=year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"
        
my_car=Car("Toyota", "Corolla", 2022)
print(my_car.display_info())

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model,year)
        self.battery_capacity=battery_capacity

    def display_info(self):
        return f"{super().display_info()} with {self.battery_capacity} kWh battery"
    
ev=ElectricCar("Tesla", "Model 5", 2023, 100)
print(ev.display_info())