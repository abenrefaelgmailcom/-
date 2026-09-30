
# OOP Inheritance Exercise
# Vehicles and Trip Cost


# 1. Parent class
class Vehicle:

    def __init__(self, name: str, base_fee: float):
        self.name = name
        self.base_fee = base_fee

    def trip_cost(self, distance_km: float) -> float:
        return self.base_fee

    def __str__(self) -> str:
        return (
            f"{self.name}: Vehicle, "
            f"base_fee: {self.base_fee}"
        )


# 2. Gasoline car
class GasCar(Vehicle):

    def __init__(
        self,
        liters_per_100km: float,
        price_per_liter: float,
        base_fee: float
    ):
        # Initialize inherited attributes.
        super().__init__("GasCar", base_fee)

        self.liters_per_100km = liters_per_100km
        self.price_per_liter = price_per_liter

    def trip_cost(self, distance_km: float) -> float:
        # Calculate fuel consumption.
        fuel_used = (
            distance_km / 100
        ) * self.liters_per_100km

        # Add fuel cost to the base fee.
        return (
            self.base_fee
            + fuel_used * self.price_per_liter
        )

    def __str__(self) -> str:
        return (
            f"{self.name}: "
            f"base_fee={self.base_fee}, "
            f"liters_per_100km={self.liters_per_100km}, "
            f"price_per_liter={self.price_per_liter}, "
            f"cost_50km={self.trip_cost(50):.2f}"
        )


# 3. Electric car
class ElectricCar(Vehicle):

    def __init__(
        self,
        kwh_per_100km: float,
        price_per_kwh: float,
        base_fee: float
    ):
        super().__init__("ElectricCar", base_fee)

        self.kwh_per_100km = kwh_per_100km
        self.price_per_kwh = price_per_kwh

    def trip_cost(self, distance_km: float) -> float:
        # Calculate energy consumption.
        energy_used = (
            distance_km / 100
        ) * self.kwh_per_100km

        return (
            self.base_fee
            + energy_used * self.price_per_kwh
        )

    def __str__(self) -> str:
        return (
            f"{self.name}: "
            f"base_fee={self.base_fee}, "
            f"kwh_per_100km={self.kwh_per_100km}, "
            f"price_per_kwh={self.price_per_kwh}, "
            f"cost_50km={self.trip_cost(50):.2f}"
        )


# 4. Taxi
class Taxi(Vehicle):

    def __init__(
        self,
        price_per_km: float,
        is_night: bool,
        base_fee: float
    ):
        super().__init__("Taxi", base_fee)

        self.price_per_km = price_per_km
        self.is_night = is_night

    def trip_cost(self, distance_km: float) -> float:
        # Calculate the regular trip cost.
        cost = (
            self.base_fee
            + distance_km * self.price_per_km
        )

        # Add a 20% night surcharge if needed.
        if self.is_night:
            cost *= 1.20

        return cost

    def __str__(self) -> str:
        return (
            f"{self.name}: "
            f"base_fee={self.base_fee}, "
            f"price_per_km={self.price_per_km}, "
            f"is_night={self.is_night}, "
            f"cost_50km={self.trip_cost(50):.2f}"
        )


# 5. Demo
if __name__ == "__main__":

    gas_car = GasCar(
        liters_per_100km=7.2,
        price_per_liter=7.1,
        base_fee=5.0
    )

    electric_car = ElectricCar(
        kwh_per_100km=16,
        price_per_kwh=1.2,
        base_fee=4.0
    )

    taxi = Taxi(
        price_per_km=3.8,
        is_night=True,
        base_fee=12.0
    )

    vehicle = Vehicle("Generic", 5.0)

    vehicles = [
        vehicle,
        gas_car,
        electric_car,
        taxi
    ]

    distance = 120

    for current_vehicle in vehicles:
        print(current_vehicle)

        cost = current_vehicle.trip_cost(distance)

        print(
            f"Trip cost for {distance} km: "
            f"{cost:.2f}"
        )

        print("-" * 40)