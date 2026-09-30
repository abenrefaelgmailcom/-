
from abc import ABC, abstractmethod


# 1. Chargeable interface
class Chargeable(ABC):

    @abstractmethod
    def charge(self):
        pass


# 2. Drivable interface
class Drivable(ABC):

    @abstractmethod
    def drive(self):
        pass


# 3. Abstract base class
class Vehicle(ABC):

    def __init__(self, model: str):
        self.model = model

    def __str__(self) -> str:
        return f"Vehicle model: {self.model}"

    @abstractmethod
    def move(self):
        pass


# 4. Electric car
class ElectricCar(Vehicle, Chargeable, Drivable):

    def __init__(self, model: str, battery_level: int):
        super().__init__(model)
        self.battery_level = battery_level

    # Override Vehicle.move()
    def move(self):
        print(f"{self.model} moves silently.")

    # Implement Chargeable.charge()
    def charge(self):
        print(f"{self.model} is charging.")

    # Implement Drivable.drive()
    def drive(self):
        print(f"{self.model} is driving.")

    # Override Vehicle.__str__()
    def __str__(self) -> str:
        return (
            f"ElectricCar: model={self.model}, "
            f"battery_level={self.battery_level}%"
        )


# 5. Electric scooter
class ElectricScooter(Vehicle, Chargeable):

    def __init__(self, model: str, max_speed: float):
        super().__init__(model)
        self.max_speed = max_speed

    # Override Vehicle.move()
    def move(self):
        print(f"{self.model} moves on two wheels.")

    # Implement Chargeable.charge()
    def charge(self):
        print(f"{self.model} is charging.")

    # Override Vehicle.__str__()
    def __str__(self) -> str:
        return (
            f"ElectricScooter: model={self.model}, "
            f"max_speed={self.max_speed} km/h"
        )


# 6. Create objects and test
if __name__ == "__main__":

    car = ElectricCar(
        model="Tesla Model 3",
        battery_level=80
    )

    scooter = ElectricScooter(
        model="Xiaomi Pro 2",
        max_speed=25
    )

    print(car)
    car.move()
    car.charge()
    car.drive()

    print()

    print(scooter)
    scooter.move()
    scooter.charge()