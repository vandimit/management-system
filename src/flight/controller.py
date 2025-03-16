from typing import Callable, Optional, Dict, Any, List

from src.flight.model import Flight, FlightInvalidError, FlightUpdateRequest
from src.flight.repository import FlightRepository, FlightRepositoryError


class FlightController:
    """Controller for flight operations."""

    def __init__(self, flight_repository: FlightRepository, view_update_callback: Optional[Callable] = None):
        """Initialize with model and optional view update callback."""
        self.flight_repository = flight_repository
        self.view_update_callback = view_update_callback

    def create_flight(self, flight_data: Dict[str, Any]) -> bool:
        """Create a new flight record."""
        # Validate data
        try:
            flight = Flight.from_json(flight_data)
        except FlightInvalidError as e:
            return False

        # Create the record
        try:
            self.flight_repository.create_flight(flight)
        except FlightRepositoryError as e:
            return False

        # Update the view if callback provided
        if self.view_update_callback:
            self.view_update_callback()

        return True

    def update_flight(self, flight_id: str, updated_data: Dict[str, Any]) -> bool:
        """Update an existing flight record."""
        # Validate data
        try:
            update_flight_request = FlightUpdateRequest.from_json(updated_data)
            update_flight_request.flight_id = flight_id
        except FlightInvalidError as e:
            return False

        # Update the record
        try:
            self.flight_repository.update_flight(update_flight_request)
        except FlightRepositoryError as e:
            return False

        # Update the view if callback provided
        if  self.view_update_callback:
            self.view_update_callback()

        return True

    def delete_flight(self, flight_id: str) -> bool:
        """Delete a flight record."""
        # Delete the record
        try:
            self.flight_repository.delete_flight(flight_id)
        except FlightRepositoryError as e:
            return False

        # Update the view if callback provided
        if self.view_update_callback:
            self.view_update_callback()

        return True

    def search_flights(self, search_term: str) -> List[Dict[str, Any]]:
        """Search for flight records."""
        try:
            return [flight.to_json() for flight in self.flight_repository.get_flights() if flight.contains_term(search_term)]
        except FlightRepositoryError as e:
            return []

    def get_all_flights(self) -> List[Dict[str, Any]]:
        """Get all flight records."""
        try:
            return [flight.to_json() for flight in self.flight_repository.get_flights()]
        except FlightRepositoryError as e:
            return []

    def get_flight_by_id(self, flight_id: str) -> Optional[Dict[str, Any]]:
        """Get a flight record by ID."""
        try:
            return self.flight_repository.get_flight(flight_id).to_json()
        except FlightRepositoryError as e:
            return None
