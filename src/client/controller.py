from typing import Optional, Callable, Dict, Any, List

from src.client.model import ClientInvalidError, Client, ClientUpdateRequest
from src.client.repository import ClientRepository, ClientRepositoryError


class ClientController:
    """Controller for client operations."""

    def __init__(self, client_repository: ClientRepository, view_update_callback: Optional[Callable] = None):
        """Initialize with model and optional view update callback."""
        self.client_repository = client_repository
        self.view_update_callback = view_update_callback

    def create_client(self, client_data: Dict[str, Any]) -> bool:
        """Create a new client record."""
        try:
            client = Client.from_json(client_data)
        except ClientInvalidError as e:
            return False

        # Create the record
        try:
            self.client_repository.create_client(client)
        except ClientRepositoryError as e:
            return False

        # Update the view if callback provided
        if self.view_update_callback:
            self.view_update_callback()

        return True

    def update_client(self, client_id: str, updated_data: Dict[str, Any]) -> bool:
        """Update an existing client record."""
        try:
            client_update_request = ClientUpdateRequest.from_json(updated_data)
            client_update_request.client_id = client_id
        except ClientInvalidError as e:
            return False

        # Update the record
        try:
            self.client_repository.update_client(client_update_request)
        except ClientRepositoryError as e:
            return False

        # Update the view if callback provided
        if self.view_update_callback:
            self.view_update_callback()

        return True

    def delete_client(self, client_id: str) -> bool:
        """Delete a client record."""
        # Delete the record
        try:
            self.client_repository.delete_client(client_id)
        except ClientRepositoryError as e:
            return False

        # Update the view if callback provided
        if self.view_update_callback:
            self.view_update_callback()

        return True

    def search_clients(self, search_term: str) -> List[Dict[str, Any]]:
        """Search for client records."""
        try:
            return [client.to_json() for client in self.client_repository.get_clients() if client.contains_term(search_term)]
        except ClientRepositoryError as e:
            return []

    def get_all_clients(self) -> List[Dict[str, Any]]:
        """Get all client records."""
        try:
            return [client.to_json() for client in self.client_repository.get_clients()]
        except ClientRepositoryError as e:
            return []

    def get_client_by_id(self, client_id: str) -> Optional[Dict[str, Any]]:
        """Get a client record by ID."""
        try:
            return self.client_repository.get_client(client_id).to_json()
        except ClientRepositoryError as e:
            return None
