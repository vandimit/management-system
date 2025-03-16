import abc
from typing import List

from src.flight.model import Flight, FlightUpdateRequest


class FlightRepository(abc.ABC):
    @abc.abstractmethod
    def get_flights(self) -> List[Flight]:
        pass

    @abc.abstractmethod
    def get_flight(self, flight_id: str) -> Flight:
        pass

    @abc.abstractmethod
    def create_flight(self, flight: Flight):
        pass

    @abc.abstractmethod
    def update_flight(self, flight: FlightUpdateRequest):
        pass

    @abc.abstractmethod
    def delete_flight(self, flight_id: str):
        pass

class FlightRepositoryError(Exception):
    pass