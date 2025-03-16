from typing import List

from pkg.json_db import KeyNotFound
from src.client.model import Client, ClientUpdateRequest
from src.client.repository import ClientRepository, ClientRepositoryError

SPACE = "Client"

class ClientRepositoryJson(ClientRepository):
    def __init__(self, json_db):
        self.json_db = json_db

    def get_clients(self) -> List[Client]:
        try:
            clients_dict = self.json_db.get([SPACE])
        except KeyNotFound:
            return []
        clients = [client for client in clients_dict.values()]
        return [Client.from_json(client) for client in clients]

    def get_client(self, client_id):
        try:
            client = self.json_db.get([SPACE, client_id])
        except KeyError:
            return None
        return client

    def create_client(self, client: Client):
        self.json_db.set([SPACE, client.client_id], client.to_json())

    def update_client(self, client_update_request: ClientUpdateRequest):
        try:
            client = self.json_db.get([SPACE, client_update_request.client_id])
        except KeyNotFound:
            raise ClientRepositoryError(f"Client with id {client_update_request.client_id} not found")
        updated_client = client_update_request.to_json()
        for key, value in updated_client.items():
            if value is not None:
                client[key] = value
        self.json_db.set([SPACE, client_update_request.client_id], client)

    def delete_client(self, client_id):
        try:
            self.json_db.delete([SPACE, client_id])
        except KeyNotFound:
            raise ClientRepositoryError(f"Client with id {client_id} not found")
