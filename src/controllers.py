from typing import Dict, List, Any, Optional, Callable
from models import ClientModel, AirlineModel, FlightModel


class ClientController:
    """Controller for client operations."""
    
    def __init__(self, model: ClientModel, view_update_callback: Optional[Callable] = None):
        """Initialize with model and optional view update callback."""
        self.model = model
        self.view_update_callback = view_update_callback
    
    def create_client(self, client_data: Dict[str, Any]) -> bool:
        """Create a new client record."""
        # Validate data
        if not self._validate_client_data(client_data):
            return False
        
        # Create the record
        success = self.model.create_client(client_data)
        
        # Update the view if callback provided
        if success and self.view_update_callback:
            self.view_update_callback()
        
        return success
    
    def update_client(self, client_id: str, updated_data: Dict[str, Any]) -> bool:
        """Update an existing client record."""
        # Validate data
        if not self._validate_client_data(updated_data):
            return False
        
        # Update the record
        success = self.model.update_client(client_id, updated_data)
        
        # Update the view if callback provided
        if success and self.view_update_callback:
            self.view_update_callback()
        
        return success
    
    def delete_client(self, client_id: str) -> bool:
        """Delete a client record."""
        # Delete the record
        success = self.model.delete_client(client_id)
        
        # Update the view if callback provided
        if success and self.view_update_callback:
            self.view_update_callback()
        
        return success
    
    def search_clients(self, search_term: str) -> List[Dict[str, Any]]:
        """Search for client records."""
        return self.model.search_clients(search_term)
    
    def get_all_clients(self) -> List[Dict[str, Any]]:
        """Get all client records."""
        return self.model.get_all_clients()
    
    def get_client_by_id(self, client_id: str) -> Optional[Dict[str, Any]]:
        """Get a client record by ID."""
        return self.model.get_client_by_id(client_id)
    
    def _validate_client_data(self, client_data: Dict[str, Any]) -> bool:
        """Validate client data."""
        # Check for required fields
        if not client_data.get("Name"):
            return False
        
        # Check ID format if provided
        if "ID" in client_data and not str(client_data["ID"]).isdigit():
            return False
        
        # Add more validation as needed
        
        return True


class AirlineController:
    """Controller for airline operations."""
    
    def __init__(self, model: AirlineModel, view_update_callback: Optional[Callable] = None):
        """Initialize with model and optional view update callback."""
        self.model = model
        self.view_update_callback = view_update_callback
    
    def create_airline(self, airline_data: Dict[str, Any]) -> bool:
        """Create a new airline record."""
        # Validate data
        if not self._validate_airline_data(airline_data):
            return False
        
        # Create the record
        success = self.model.create_airline(airline_data)
        
        # Update the view if callback provided
        if success and self.view_update_callback:
            self.view_update_callback()
        
        return success
    
    def update_airline(self, airline_id: str, updated_data: Dict[str, Any]) -> bool:
        """Update an existing airline record."""
        # Validate data
        if not self._validate_airline_data(updated_data):
            return False
        
        # Update the record
        success = self.model.update_airline(airline_id, updated_data)
        
        # Update the view if callback provided
        if success and self.view_update_callback:
            self.view_update_callback()
        
        return success
    
    def delete_airline(self, airline_id: str) -> bool:
        """Delete an airline record."""
        # Delete the record
        success = self.model.delete_airline(airline_id)
        
        # Update the view if callback provided
        if success and self.view_update_callback:
            self.view_update_callback()
        
        return success
    
    def search_airlines(self, search_term: str) -> List[Dict[str, Any]]:
        """Search for airline records."""
        return self.model.search_airlines(search_term)
    
    def get_all_airlines(self) -> List[Dict[str, Any]]:
        """Get all airline records."""
        return self.model.get_all_airlines()
    
    def get_airline_by_id(self, airline_id: str) -> Optional[Dict[str, Any]]:
        """Get an airline record by ID."""
        return self.model.get_airline_by_id(airline_id)
    
    def _validate_airline_data(self, airline_data: Dict[str, Any]) -> bool:
        """Validate airline data."""
        # Check for required fields
        if not airline_data.get("Company Name"):
            return False
        
        # Check ID format if provided
        if "ID" in airline_data and not str(airline_data["ID"]).isdigit():
            return False
        
        # Validate IATA code if provided (should be 2 letters)
        if "IATA Code" in airline_data and airline_data["IATA Code"]:
            iata_code = airline_data["IATA Code"]
            if len(iata_code) != 2 or not iata_code.isalpha():
                return False
        
        return True


class FlightController:
    """Controller for flight operations."""
    
    def __init__(self, model: FlightModel, view_update_callback: Optional[Callable] = None):
        """Initialize with model and optional view update callback."""
        self.model = model
        self.view_update_callback = view_update_callback
    
    def create_flight(self, flight_data: Dict[str, Any]) -> bool:
        """Create a new flight record."""
        # Validate data
        if not self._validate_flight_data(flight_data):
            return False
        
        # Create the record
        success = self.model.create_flight(flight_data)
        
        # Update the view if callback provided
        if success and self.view_update_callback:
            self.view_update_callback()
        
        return success
    
    def update_flight(self, flight_id: str, updated_data: Dict[str, Any]) -> bool:
        """Update an existing flight record."""
        # Validate data
        if not self._validate_flight_data(updated_data):
            return False
        
        # Update the record
        success = self.model.update_flight(flight_id, updated_data)
        
        # Update the view if callback provided
        if success and self.view_update_callback:
            self.view_update_callback()
        
        return success
    
    def delete_flight(self, flight_id: str) -> bool:
        """Delete a flight record."""
        # Delete the record
        success = self.model.delete_flight(flight_id)
        
        # Update the view if callback provided
        if success and self.view_update_callback:
            self.view_update_callback()
        
        return success
    
    def search_flights(self, search_term: str) -> List[Dict[str, Any]]:
        """Search for flight records."""
        return self.model.search_flights(search_term)
    
    def get_all_flights(self) -> List[Dict[str, Any]]:
        """Get all flight records."""
        return self.model.get_all_flights()
    
    def get_flight_by_id(self, flight_id: str) -> Optional[Dict[str, Any]]:
        """Get a flight record by ID."""
        return self.model.get_flight_by_id(flight_id)
    
    def _validate_flight_data(self, flight_data: Dict[str, Any]) -> bool:
        """Validate flight data."""
        # Check for required fields
        required_fields = ["Flight ID", "Client ID", "Airline ID", "Date", "Departure", "Arrival"]
        for field in required_fields:
            if not flight_data.get(field):
                return False
        
        # Validate date format (basic check)
        date_str = flight_data.get("Date", "")
        date_parts = date_str.split("-")
        if len(date_parts) != 3:
            return False
        
        # Add more validation as needed
        
        return True
