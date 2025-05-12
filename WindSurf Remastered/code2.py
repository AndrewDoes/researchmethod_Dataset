"""
Basic example of a Vehicle registration system.
"""

from dataclasses import dataclass
from enum import Enum, auto
from random import choices
from string import ascii_uppercase, digits
from typing import List

# Constants
TAX_RATES = {
    FuelType.ELECTRIC: 0.02,
    FuelType.PETROL: 0.05,
}

# Enums
class FuelType(Enum):
    """Types of fuel used in a vehicle."""

    ELECTRIC = auto()
    PETROL = auto()

class RegistryStatus(Enum):
    """Possible statuses for the vehicle registry system."""

    ONLINE = auto()
    CONNECTION_ERROR = auto()
    OFFLINE = auto()

# Data classes
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
        return TAX_RATES[self.fuel_type] * self.catalogue_price

    def get_info_str(self) -> str:
        """String representation of this instance."""
        return f"Brand: {self.brand} - Model: {self.model} - Tax: {self.tax}"

@dataclass
class Vehicle:
    """Class representing a vehicle (electric or fossil fuel)."""

    vehicle_id: str
    license_plate: str
    info: VehicleModelInfo

    def to_string(self) -> str:
        """String representation of this instance."""
        info_str = self.info.get_info_str()
        return f"Id: {self.vehicle_id}. License plate: {self.license_plate}. Info: {info_str}."

# Custom exception
class VehicleInfoMissingError(Exception):
    """Custom error that is raised when vehicle information is missing for a particular brand."""

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.message = f"Vehicle information is missing for {brand} {model}."
        super().__init__(self.message)

# Vehicle registry class
class VehicleRegistry:
    """Class representing a basic vehicle registration system."""

    def __init__(self) -> None:
        self.vehicle_models: List[VehicleModelInfo] = []
        self.online = True

    def add_vehicle_model_info(self, brand: str, model: str, catalogue_price: int, fuel_type: FuelType, year: int) -> None:
        """Helper method for adding a VehicleModelInfo object to a list."""
        self.vehicle_models.append(VehicleModelInfo(brand, model, catalogue_price, fuel_type, year))

    def generate_vehicle_id(self, length: int) -> str:
        """Helper method for generating a random vehicle id."""
        return "".join(choices(ascii_uppercase, k=length))

    def generate_vehicle_license(self, _id: str) -> str:
        """Helper method for generating a vehicle license number."""
        return f"{_id[:2]}-{''.join(choices(digits, k=2))}-{''.join(choices(ascii_uppercase, k=2))}"

    def register_vehicle(self, brand: str, model: str) -> Vehicle:
        """Create a new vehicle and generate an id and a license plate."""
        for vehicle_model in self.vehicle_models:
            if vehicle_model.brand == brand and vehicle_model.model == model:
                vehicle_id = self.generate_vehicle_id(12)
                license_plate = self.generate_vehicle_license(vehicle_id)
                return Vehicle(vehicle_id, license_plate, vehicle_model)
        raise VehicleInfoMissingError(brand, model)

    def online_status(self) -> RegistryStatus:
        """Report whether the registry system is online."""
        if not self.online:
            return RegistryStatus.OFFLINE
        elif len(self.vehicle_models) == 0:
            return RegistryStatus.CONNECTION_ERROR
        else:
            return RegistryStatus.ONLINE

# Main function
def main() -> None:
    registry = VehicleRegistry()

    # Add vehicle models
    registry.add_vehicle_model_info("Tesla", "Model 3", 50000, FuelType.ELECTRIC, 2021)
    registry.add_vehicle_model_info("Volkswagen", "ID3", 35000, FuelType.ELECTRIC, 2021)
    registry.add_vehicle_model_info("BMW", "520e", 60000, FuelType.PETROL, 2021)
    registry.add_vehicle_model_info("Tesla", "Model Y", 55000, FuelType.ELECTRIC, 2021)

    # Verify that the registry is online
    print(f"Registry status: {registry.online_status()}")

    # Register a new vehicle
    vehicle = registry.register_vehicle("Volkswagen", "ID3")

    #