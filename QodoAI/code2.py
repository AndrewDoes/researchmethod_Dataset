"""
Advanced Vehicle Registration System.
"""

from dataclasses import dataclass
from enum import Enum, auto
from random import choices
from string import ascii_uppercase, digits


class FuelType(Enum):
    """Types of fuel used in a vehicle."""
    ELECTRIC = auto()
    PETROL = auto()


class RegistryStatus(Enum):
    """Possible statuses for the vehicle registry system."""
    ONLINE = auto()
    CONNECTION_ERROR = auto()
    OFFLINE = auto()


TAX_RATES = {FuelType.ELECTRIC: 0.02, FuelType.PETROL: 0.05}


@dataclass
class VehicleInfoMissingError(Exception):
    """Custom error raised when vehicle information is missing for a particular brand."""
    brand: str
    model: str
    message: str = "Vehicle information is missing."


@dataclass
class VehicleModelInfo:
    """Class containing basic information about a vehicle model."""
    brand: str
    model: str
    catalogue_price: int
    fuel_type: FuelType
    production_year: int

    @property
    def tax(self) -> float:
        """Calculate tax to be paid when registering a vehicle of this type."""
        return TAX_RATES[self.fuel_type] * self.catalogue_price

    def get_info_str(self) -> str:
        """String representation of this instance."""
        return f"brand: {self.brand} - type: {self.model} - tax: {self.tax}"


@dataclass
class Vehicle:
    """Class representing a vehicle (electric or fossil fuel)."""
    vehicle_id: str
    license_plate: str
    info: VehicleModelInfo

    def to_string(self) -> str:
        """String representation of this instance."""
        return f"Id: {self.vehicle_id}. License plate: {self.license_plate}. Info: {self.info.get_info_str()}."


class VehicleRegistry:
    """Class representing a basic vehicle registration system."""

    def __init__(self) -> None:
        self.vehicle_models: list[VehicleModelInfo] = []
        self.online = True

    def add_vehicle_model_info(self, brand: str, model: str, catalogue_price: int, fuel_type: FuelType, year: int) -> None:
        """Add a VehicleModelInfo object to the registry."""
        self.vehicle_models.append(VehicleModelInfo(brand, model, catalogue_price, fuel_type, year))

    def generate_vehicle_id(self, length: int = 12) -> str:
        """Generate a random vehicle ID."""
        return "".join(choices(ascii_uppercase, k=length))

    def generate_vehicle_license(self, vehicle_id: str) -> str:
        """Generate a vehicle license number."""
        return f"{vehicle_id[:2]}-{''.join(choices(digits, k=2))}-{''.join(choices(ascii_uppercase, k=2))}"

    def register_vehicle(self, brand: str, model: str) -> Vehicle:
        """Create a new vehicle and generate an ID and a license plate."""
        vehicle_info = self._find_vehicle_info(brand, model)
        vehicle_id = self.generate_vehicle_id()
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, vehicle_info)

    def _find_vehicle_info(self, brand: str, model: str) -> VehicleModelInfo:
        """Find vehicle information by brand and model."""
        for vehicle_info in self.vehicle_models:
            if vehicle_info.brand == brand and vehicle_info.model == model:
                return vehicle_info
        raise VehicleInfoMissingError(brand, model)

    def online_status(self) -> RegistryStatus:
        """Report whether the registry system is online."""
        if not self.online:
            return RegistryStatus.OFFLINE
        if not self.vehicle_models:
            return RegistryStatus.CONNECTION_ERROR
        return RegistryStatus.ONLINE


def main() -> None:
    """Main function to demonstrate the Vehicle Registration System."""
    registry = VehicleRegistry()

    # Add vehicle models
    registry.add_vehicle_model_info("Tesla", "Model 3", 50000, FuelType.ELECTRIC, 2021)
    registry.add_vehicle_model_info("Volkswagen", "ID3", 35000, FuelType.ELECTRIC, 2021)
    registry.add_vehicle_model_info("BMW", "520e", 60000, FuelType.PETROL, 2021)
    registry.add_vehicle_model_info("Tesla", "Model Y", 55000, FuelType.ELECTRIC, 2021)

    # Verify registry status
    print(f"Registry status: {registry.online_status()}")

    # Register a new vehicle
    vehicle = registry.register_vehicle("Volkswagen", "ID3")

    # Print vehicle information
    print(vehicle.to_string())


if __name__ == "__main__":
    main()