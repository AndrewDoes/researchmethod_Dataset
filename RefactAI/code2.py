"""
Basic example of a Vehicle registration system.
"""
from dataclasses import dataclass
from enum import Enum, auto
from random import choices
from string import ascii_uppercase, digits
from typing import List


class FuelType(Enum):
    """Types of fuel used in a vehicle."""
    ELECTRIC = auto()
    PETROL = auto()


class RegistryStatus(Enum):
    """Possible statuses for the vehicle registry system."""
    ONLINE = auto()
    CONNECTION_ERROR = auto()
    OFFLINE = auto()


taxes = {FuelType.ELECTRIC: 0.02, FuelType.PETROL: 0.05}


class VehicleInfoMissingError(Exception):
    """Custom error that is raised when vehicle information is missing for a particular brand/model."""
    def __init__(self, brand: str, model: str, message: str = "Vehicle information is missing."):
        self.brand = brand
        self.model = model
        self.message = message
        super().__init__(f"{message} Brand: {brand}, Model: {model}")


@dataclass
class VehicleModelInfo:
    """Class that contains basic information about a vehicle model."""
    brand: str
    model: str
    catalogue_price: int
    fuel_type: FuelType
    production_year: int

    @property
    def tax(self) -> float:
        """Tax to be paid when registering a vehicle of this type."""
        tax_percentage = taxes[self.fuel_type]
        return tax_percentage * self.catalogue_price

    def __str__(self) -> str:
        return f"brand: {self.brand} - type: {self.model} - tax: {self.tax:.2f}"

    def get_info_str(self) -> str:
        """String representation of this instance."""
        return str(self)


@dataclass
class Vehicle:
    """Class representing a vehicle (electric or fossil fuel)."""
    vehicle_id: str
    license_plate: str
    info: VehicleModelInfo

    def __str__(self) -> str:
        return f"Id: {self.vehicle_id}. License plate: {self.license_plate}. Info: {self.info}"

    def to_string(self) -> str:
        """String representation of this instance."""
        return str(self)


class VehicleRegistry:
    """Class representing a basic vehicle registration system."""

    def __init__(self) -> None:
        self.vehicle_models: List[VehicleModelInfo] = []
        self.online = True

    def add_vehicle_model_info(
        self,
        brand: str,
        model: str,
        catalogue_price: int,
        fuel_type: FuelType,
        year: int,
    ) -> None:
        """Helper method for adding a VehicleModelInfo object to a list."""
        self.vehicle_models.append(
            VehicleModelInfo(brand, model, catalogue_price, fuel_type, year)
        )

    def generate_vehicle_id(self, length: int) -> str:
        """Helper method for generating a random vehicle id."""
        return "".join(choices(ascii_uppercase, k=length))

    def generate_vehicle_license(self, _id: str) -> str:
        """Helper method for generating a vehicle license number."""
        return f"{_id[:2]}-{''.join(choices(digits, k=2))}-{''.join(choices(ascii_uppercase, k=2))}"

    def register_vehicle(self, brand: str, model: str) -> Vehicle:
        """Create a new vehicle and generate an id and a license plate."""
        vehicle_info = next(
            (v for v in self.vehicle_models if v.brand == brand and v.model == model), None
        )
        if vehicle_info is None:
            raise VehicleInfoMissingError(brand, model)
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, vehicle_info)

    def online_status(self) -> RegistryStatus:
        """Report whether the registry system is online."""
        if not self.online:
            return RegistryStatus.OFFLINE
        if not self.vehicle_models:
            return RegistryStatus.CONNECTION_ERROR
        return RegistryStatus.ONLINE


if __name__ == "__main__":

    # create a registry instance
    registry = VehicleRegistry()

    # add a couple of different vehicle models
    registry.add_vehicle_model_info("Tesla", "Model 3", 50000, FuelType.ELECTRIC, 2021)
    registry.add_vehicle_model_info("Volkswagen", "ID3", 35000, FuelType.ELECTRIC, 2021)
    registry.add_vehicle_model_info("BMW", "520e", 60000, FuelType.PETROL, 2021)
    registry.add_vehicle_model_info("Tesla", "Model Y", 55000, FuelType.ELECTRIC, 2021)

    # verify that the registry is online
    print(f"Registry status: {registry.online_status()}")

    # register a new vehicle
    vehicle = registry.register_vehicle("Volkswagen", "ID3")

    # print out the vehicle information
    print(vehicle)