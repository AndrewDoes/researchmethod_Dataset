from dataclasses import dataclass
from enum import Enum, auto
from random import choices
from string import ascii_uppercase, digits
from typing import List

# Define a custom error for missing vehicle information
class VehicleInfoMissingError(Exception):
    def __init__(self, brand: str, model: str):
        self.message = f"Vehicle information is missing for {brand} {model}"
        super().__init__(self.message)

# Define an Enum for fuel types
class FuelType(Enum):
    ELECTRIC = auto()
    PETROL = auto()

# Define an Enum for registry statuses
class RegistryStatus(Enum):
    ONLINE = auto()
    CONNECTION_ERROR = auto()
    OFFLINE = auto()

# Define a dataclass for vehicle model information
@dataclass
class VehicleModelInfo:
    brand: str
    model: str
    catalogue_price: int
    fuel_type: FuelType
    production_year: int

    @property
    def tax(self) -> float:
        """Calculate the tax for this vehicle model"""
        tax_percentage = {
            FuelType.ELECTRIC: 0.02,
            FuelType.PETROL: 0.05,
        }[self.fuel_type]
        return tax_percentage * self.catalogue_price

    def get_info_str(self) -> str:
        """Return a string representation of this vehicle model"""
        return f"Brand: {self.brand}, Model: {self.model}, Tax: {self.tax}"

# Define a dataclass for vehicles
@dataclass
class Vehicle:
    vehicle_id: str
    license_plate: str
    info: VehicleModelInfo

    def to_string(self) -> str:
        """Return a string representation of this vehicle"""
        info_str = self.info.get_info_str()
        return f"ID: {self.vehicle_id}, License Plate: {self.license_plate}, Info: {info_str}"

# Define a class for the vehicle registry
class VehicleRegistry:
    def __init__(self):
        self.vehicle_models: List[VehicleModelInfo] = []
        self.online = True

    def add_vehicle_model_info(self, brand: str, model: str, catalogue_price: int, fuel_type: FuelType, year: int) -> None:
        """Add a vehicle model to the registry"""
        self.vehicle_models.append(VehicleModelInfo(brand, model, catalogue_price, fuel_type, year))

    def generate_vehicle_id(self, length: int) -> str:
        """Generate a random vehicle ID"""
        return "".join(choices(ascii_uppercase, k=length))

    def generate_vehicle_license(self, _id: str) -> str:
        """Generate a vehicle license plate"""
        return f"{_id[:2]}-{''.join(choices(digits, k=2))}-{''.join(choices(ascii_uppercase, k=2))}"

    def register_vehicle(self, brand: str, model: str) -> Vehicle:
        """Register a new vehicle"""
        for vehicle_info in self.vehicle_models:
            if vehicle_info.brand == brand and vehicle_info.model == model:
                vehicle_id = self.generate_vehicle_id(12)
                license_plate = self.generate_vehicle_license(vehicle_id)
                return Vehicle(vehicle_id, license_plate, vehicle_info)
        raise VehicleInfoMissingError(brand, model)

    def online_status(self) -> RegistryStatus:
        """Check the registry's online status"""
        if not self.online:
            return RegistryStatus.OFFLINE
        elif not self.vehicle_models:
            return RegistryStatus.CONNECTION_ERROR
        return RegistryStatus.ONLINE

# Example usage
if __name__ == "__main__":
    registry = VehicleRegistry()

    registry.add_vehicle_model_info("Tesla", "Model 3", 50000, FuelType.ELECTRIC, 2021)
    registry.add_vehicle_model_info("Volkswagen", "ID3", 35000, FuelType.ELECTRIC, 2021)
    registry.add_vehicle_model_info("BMW", "520e", 60000, FuelType.PETROL, 2021)
    registry.add_vehicle_model_info("Tesla", "Model Y", 55000, FuelType.ELECTRIC, 2021)

    print(f"Registry status: {registry.online_status()}")

    vehicle = registry.register_vehicle("Volkswagen", "ID3")
    print(vehicle.to_string())