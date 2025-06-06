"""
Basic example of a Vehicle registration system.
"""

from dataclasses import dataclass
from enum import Enum, auto
from random import choices
from string import ascii_uppercase, digits
from typing import List, Optional


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
    """Custom error that is raised when vehicle information is missing for a particular brand."""
    brand: str
    model: str
    message: str = "Vehicle information is missing."


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
        return self.get_tax_rate() * self.catalogue_price

    def get_tax_rate(self) -> float:
        """Get the tax rate for the vehicle's fuel type."""
        return TAX_RATES.get(self.fuel_type, 0.0)

    def __str__(self) -> str:
        """String representation of this instance."""
        return f"brand: {self.brand} - type: {self.model} - tax: {self.tax}"

@dataclass
class Vehicle:
    """Class representing a vehicle (electric or fossil fuel)."""
    vehicle_id: str
    license_plate: str
    info: VehicleModelInfo

    def __str__(self) -> str:
        """String representation of this instance."""
        return (
            f"Id: {self.vehicle_id}. "
            f"License plate: {self.license_plate}. "
            f"Info: {self.info}."
        )


class VehicleRegistry:
    """Class representing a basic vehicle registration system."""

    def __init__(self) -> None:
        self.vehicle_models: List[VehicleModelInfo] = []
        self.online: bool = True

    def add_vehicle_model_info(
        self,
        brand: str,
        model: str,
        catalogue_price: int,
        fuel_type: FuelType,
        year: int,
    ) -> None:
        """Add a VehicleModelInfo object to the registry."""
        self.vehicle_models.append(
            VehicleModelInfo(brand, model, catalogue_price, fuel_type, year)
        )

    def generate_vehicle_id(self, length: int = 12) -> str:
        """Generate a random vehicle id."""
        return "".join(choices(ascii_uppercase, k=length))

    def generate_vehicle_license(self, vehicle_id: str) -> str:
        """Generate a vehicle license number."""
        return (
            f"{vehicle_id[:2]}-"
            f"{''.join(choices(digits, k=2))}-"
            f"{''.join(choices(ascii_uppercase, k=2))}"
        )

    def find_vehicle_model_info(self, brand: str, model: str) -> Optional[VehicleModelInfo]:
        """Find vehicle model info by brand and model."""
        return next(
            (info for info in self.vehicle_models if info.brand == brand and info.model == model),
            None
        )

    def register_vehicle(self, brand: str, model: str) -> Vehicle:
        """Create a new vehicle and generate an id and a license plate."""
        vehicle_info = self.find_vehicle_model_info(brand, model)
        if not vehicle_info:
            raise VehicleInfoMissingError(brand, model)
        vehicle_id = self.generate_vehicle_id()
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, vehicle_info)

    def online_status(self) -> RegistryStatus:
        """Report whether the registry system is online."""
        if not self.online:
            return RegistryStatus.OFFLINE
        if not self.vehicle_models:
            return RegistryStatus.CONNECTION_ERROR
        return RegistryStatus.ONLINE


def main() -> None:
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


if __name__ == "__main__":
    main()