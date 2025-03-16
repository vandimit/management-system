from typing import List

from pkg.json_db import JsonFileDB, KeyNotFound
from src.flight.model import FlightUpdateRequest, Flight
from src.flight.repository import FlightRepository, FlightRepositoryError

SPACE = "Flight"

class FlightRepositoryJson(FlightRepository):
    def __init__(self, json_db: JsonFileDB):
        self.json_db = json_db

    def get_flights(self) -> List[Flight]:
        try:
            flights_dict = self.json_db.get([SPACE])
        except KeyNotFound:
            return []
        flights = [flight for flight in flights_dict.values()]
        return [Flight.from_json(flight) for flight in flights]

    def get_flight(self, flight_id: str):
        try:
            flight = self.json_db.get([SPACE, flight_id])
        except KeyNotFound:
            raise FlightRepositoryError(f"Flight with id {flight_id} not found")
        return Flight.from_json(flight)

    def create_flight(self, flight: Flight):
        self.json_db.set([SPACE, flight.flight_id], flight.to_json())

    def update_flight(self, flight_update_request: FlightUpdateRequest):
        try:
            flight = self.json_db.get([SPACE, flight_update_request.flight_id])
        except KeyNotFound:
            raise FlightRepositoryError(f"Flight with id {flight_update_request.flight_id} not found")

        updated_flight = flight_update_request.to_json()
        for key, value in updated_flight.items():
            if value is not None:
                flight[key] = value

        self.json_db.set([SPACE, flight_update_request.flight_id], flight)


    def delete_flight(self, flight_id: str):
        try:
            self.json_db.delete([SPACE, flight_id])
        except KeyNotFound:
            raise FlightRepositoryError(f"Flight with id {flight_id} not found")
