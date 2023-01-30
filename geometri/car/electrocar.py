from geometri.car import carclass


class Electrocar(carclass.CarClass):
    def __init__(self, brand, model, year, probeg):
        self.battery = 100
        super().__init__(brand, model, year, probeg)

    def deascription_battery(self):
        print(f"Мощность {self.battery}%")
