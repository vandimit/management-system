import abc
from typing import List

from src.airline.model import Airline, AirlineUpdateRequest


class AirlineRepository(abc.ABC):
    @abc.abstractmethod
    def get_airlines(self) -> List[Airline]:
        pass

    @abc.abstractmethod
    def get_airline(self, airline_id: str):
        pass

    @abc.abstractmethod
    def create_airline(self, airline: Airline):
        pass

    @abc.abstractmethod
    def update_airline(self, airline_update_request: AirlineUpdateRequest):
        pass

    @abc.abstractmethod
    def delete_airline(self, airline_id: str):
        pass

class AirlineRepositoryError(Exception):
    pass
