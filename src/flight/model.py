import dataclasses
from typing import Dict, Any, Optional

from pkg.json_object import JSONObject

ID = "Flight ID"
CLIENT_ID = "Client ID"
AIRLINE_ID = "Airline ID"
DATE = "Date"
DEPARTURE = "Departure"
ARRIVAL = "Arrival"
STATUS = "Status"

@dataclasses.dataclass
class Flight(JSONObject):
    flight_id: str
    client_id: str
    airline_id: str
    date: str
    departure: str
    arrival: str
    status: str

    def to_json(self) -> Dict[str, Any]:
        return {
            ID: self.flight_id,
            CLIENT_ID: self.client_id,
            AIRLINE_ID: self.airline_id,
            DATE: self.date,
            DEPARTURE: self.departure,
            ARRIVAL: self.arrival,
            STATUS: self.status
        }

    @classmethod
    def from_json(cls, json: Dict[str, Any]) -> 'Flight':
        required_fields = [ID, CLIENT_ID, AIRLINE_ID, DATE, DEPARTURE, ARRIVAL]
        for field in required_fields:
            if not json.get(field):
                raise FlightInvalidError(f"{field} is required.")

        # Validate date format (basic check)
        date_str = json.get(DATE, "")
        date_parts = date_str.split("-")
        if len(date_parts) != 3:
            raise FlightInvalidError("Invalid date format. Use YYYY-MM-DD.")

        return cls(
            flight_id=json.get(ID),
            client_id=json.get(CLIENT_ID, ""),
            airline_id=json.get(AIRLINE_ID, ""),
            date=json.get(DATE, ""),
            departure=json.get(DEPARTURE, ""),
            arrival=json.get(ARRIVAL, ""),
            status=json.get(STATUS, "")
        )

@dataclasses.dataclass
class FlightUpdateRequest(JSONObject):
    flight_id: str
    client_id: Optional[str] = None
    airline_id: Optional[str] = None
    date: Optional[str] = None
    departure: Optional[str] = None
    arrival: Optional[str] = None
    status: Optional[str] = None

    def to_json(self) -> Dict[str, Any]:
        return {
            ID: self.flight_id,
            CLIENT_ID: self.client_id,
            AIRLINE_ID: self.airline_id,
            DATE: self.date,
            DEPARTURE: self.departure,
            ARRIVAL: self.arrival,
            STATUS: self.status
        }

    @classmethod
    def from_json(cls, json: Dict[str, Any]) -> 'FlightUpdateRequest':
        if not json.get(ID):
            raise FlightInvalidError("Flight ID is required.")
        return cls(
            flight_id=json.get(ID),
            client_id=json.get(CLIENT_ID),
            airline_id=json.get(AIRLINE_ID),
            date=json.get(DATE),
            departure=json.get(DEPARTURE),
            arrival=json.get(ARRIVAL),
            status=json.get(STATUS)
        )

class FlightInvalidError(Exception):
    pass
