import abc
from typing import List

from src.client.model import Client, ClientUpdateRequest


class ClientRepository(abc.ABC):
    @abc.abstractmethod
    def get_clients(self) -> List[Client]:
        pass

    @abc.abstractmethod
    def get_client(self, client_id: str) -> Client:
        pass

    @abc.abstractmethod
    def create_client(self, client: Client):
        pass

    @abc.abstractmethod
    def update_client(self, client: ClientUpdateRequest):
        pass

    @abc.abstractmethod
    def delete_client(self, client_id: str):
        pass

class ClientRepositoryError(Exception):
    pass
