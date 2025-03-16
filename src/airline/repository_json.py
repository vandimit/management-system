from typing import List

from pkg.json_db import JsonFileDB, KeyNotFound
from src.airline.model import AirlineUpdateRequest, Airline
from src.airline.repository import AirlineRepository, AirlineRepositoryError

SPACE = "Airline"

class AirlineRepositoryJson(AirlineRepository):
    def __init__(self, json_db: JsonFileDB):
        self.json_db = json_db

    def get_airlines(self) -> List[Airline]:
        try:
            airlines_dict = self.json_db.get([SPACE])
        except KeyNotFound:
            return []
        airlines = [airline for airline in airlines_dict.values()]
        return [Airline.from_json(airline) for airline in airlines]

    def get_airline(self, airline_id: str):
        try:
            airline = self.json_db.get([SPACE, airline_id])
        except KeyNotFound:
            raise AirlineRepositoryError(f"Airline with id {airline_id} not found")
        return Airline.from_json(airline)

    def create_airline(self, airline: Airline):
        self.json_db.set([SPACE, airline.airline_id], airline.to_json())

    def update_airline(self, airline_update_request: AirlineUpdateRequest):
        try:
            airline = self.json_db.get([SPACE, airline_update_request.airline_id])
        except KeyNotFound:
            raise AirlineRepositoryError(f"Airline with id {airline_update_request.airline_id} not found")

        updated_airline = airline_update_request.to_json()
        for key, value in updated_airline.items():
            if value is not None:
                airline[key] = value

        self.json_db.set([SPACE, airline_update_request.airline_id], airline)


    def delete_airline(self, airline_id: str):
        try:
            self.json_db.delete([SPACE, airline_id])
        except KeyNotFound:
            raise AirlineRepositoryError(f"Airline with id {airline_id} not found")
