from typing import Callable, Optional, Dict, Any, List

from src.airline.model import Airline, AirlineInvalidError, AirlineUpdateRequest
from src.airline.repository import AirlineRepository, AirlineRepositoryError


class AirlineController:
    """Controller for airline operations."""

    def __init__(self, airline_repository: AirlineRepository, view_update_callback: Optional[Callable] = None):
        """Initialize with model and optional view update callback."""
        self.airline_repository = airline_repository
        self.view_update_callback = view_update_callback

    def create_airline(self, airline_data: Dict[str, Any]) -> bool:
        """Create a new airline record."""
        # Validate data
        try:
            airline = Airline.from_json(airline_data)
        except AirlineInvalidError as e:
            return False

        # Create the record
        try:
            self.airline_repository.create_airline(airline)
        except AirlineRepositoryError as e:
            return False

        # Update the view if callback provided
        if self.view_update_callback:
            self.view_update_callback()

        return True

    def update_airline(self, airline_id: str, updated_data: Dict[str, Any]) -> bool:
        """Update an existing airline record."""
        # Validate data
        try:
            airline_update_request = AirlineUpdateRequest.from_json(updated_data)
            airline_update_request.id = airline_id
        except AirlineInvalidError as e:
            return False

        # Update the record
        try:
            self.airline_repository.update_airline(airline_update_request)
        except AirlineRepositoryError as e:
            return False

        # Update the view if callback provided
        if self.view_update_callback:
            self.view_update_callback()

        return True

    def delete_airline(self, airline_id: str) -> bool:
        """Delete an airline record."""
        # Delete the record
        try:
            self.airline_repository.delete_airline(airline_id)
        except AirlineRepositoryError as e:
            return False

        # Update the view if callback provided
        if self.view_update_callback:
            self.view_update_callback()

        return True

    def search_airlines(self, search_term: str) -> List[Dict[str, Any]]:
        """Search for airline records."""
        try:
            return [airline.to_json() for airline in self.airline_repository.get_airlines() if airline.contains_term(search_term)]
        except AirlineRepositoryError as e:
            return []

    def get_all_airlines(self) -> List[Dict[str, Any]]:
        """Get all airline records."""
        try:
            return [airline.to_json() for airline in self.airline_repository.get_airlines()]
        except AirlineRepositoryError as e:
            return []

    def get_airline_by_id(self, airline_id: str) -> Optional[Dict[str, Any]]:
        """Get an airline record by ID."""
        try:
            return self.airline_repository.get_airline(airline_id).to_json()
        except AirlineRepositoryError as e:
            return None
