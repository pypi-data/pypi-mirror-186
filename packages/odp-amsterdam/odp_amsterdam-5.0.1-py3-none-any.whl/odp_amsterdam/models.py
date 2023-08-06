"""Models for Open Data Platform of Amsterdam."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .const import CORRECTIONS, FILTER_NAMES, FILTER_UNKNOWN


@dataclass
class ParkingSpot:
    """Object representing an ParkingSpot model response from the API."""

    spot_id: str
    spot_type: str | None
    spot_description: str | None

    street: str | None
    number: int | None
    orientation: str | None

    coordinates: list[float]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> ParkingSpot:
        """Return ParkingSpot object from a dictionary.

        Args:
            data: The JSON data from the API.

        Returns:
            An ParkingSpot object.
        """
        attr = data["properties"]
        regimes = attr["regimes"][0]
        return cls(
            spot_id=attr["id"],
            spot_type=attr["eType"] or None,
            spot_description=regimes["eTypeDescription"] or None,
            street=filter_unknown(attr["straatnaam"]),
            number=int(attr["aantal"]),
            orientation=filter_unknown(attr["type"]),
            coordinates=data["geometry"]["coordinates"],
        )


@dataclass
class Garage:
    """Object representing an Garage model response from the API."""

    garage_id: str
    garage_name: str
    state: str
    free_space_short: int
    free_space_long: int | None
    short_capacity: int
    long_capacity: int | None
    availability_pct: float
    longitude: float
    latitude: float

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> Garage:
        """Return Garage object from a dictionary.

        Args:
            data: The JSON data from the API.

        Returns:
            An Garage object.
        """
        latitude, longitude = split_coordinates(str(data["geometry"]["coordinates"]))
        attr = data["properties"]
        return cls(
            garage_id=data["Id"],
            garage_name=correct_name(data["properties"]["Name"]),
            state=attr.get("State"),
            free_space_short=attr.get("FreeSpaceShort"),
            free_space_long=attr.get("FreeSpaceLong", None),
            short_capacity=attr.get("ShortCapacity"),
            long_capacity=attr.get("LongCapacity", None),
            availability_pct=round(
                (float(attr.get("FreeSpaceShort")) / float(attr.get("ShortCapacity")))
                * 100,
                1,
            ),
            longitude=longitude,
            latitude=latitude,
        )


def split_coordinates(data: str) -> tuple[float, float]:
    """Split the coordinate data in separate variables.

    Args:
        data: The data to be split.

    Returns:
        The coordinates.
    """

    longitude, latitude = data.split(", ")
    longitude = longitude.replace("[", "")
    latitude = latitude.replace("]", "")
    return float(latitude), float(longitude)


def correct_name(name: str) -> str:
    """Change parking garage name for consistency if needed.

    Args:
        name: The name of the parking garage.

    Returns:
        The corrected name.
    """

    for value in FILTER_NAMES:
        # Remove parts from name string.
        name = name.replace(value, "")

    if any(y in name for y in CORRECTIONS):
        # Add a 0 for consistency.
        return name[:1] + "0" + name[1:]
    return name


def filter_unknown(data: str) -> str | None:
    """Filter unknown data from the API.

    Args:
        data: The data to be filtered.

    Returns:
        The filtered data.
    """
    if data in FILTER_UNKNOWN:
        return None
    return data
