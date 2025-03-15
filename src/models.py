import json
import os
from typing import Dict, List, Optional, Any

class RecordModel:
    """Base class for record management models."""
    
    def __init__(self, ctx, data_file: str = 'records.json'):
        """Initialize with path to data file."""
        self.data_file = data_file
        self.records = self.load_records()
        self.ctx = ctx
    
    def load_records(self) -> Dict[str, List[Dict[str, Any]]]:
        """Load records from JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            else:
                # Return empty structure if file doesn't exist
                return {"Client": [], "Airline": [], "Flight": []}
        except Exception as e:
            print(f"Error loading records: {e}")
            return {"Client": [], "Airline": [], "Flight": []}
    
    def save_records(self) -> bool:
        """Save records to JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.records, file, indent=4)
            return True
        except Exception as e:
            print(f"Error saving records: {e}")
            return False


class ClientModel(RecordModel):
    """Model for Client records."""

    def __init__(self, ctx):
        super().__init__(ctx=ctx)

    def create_client(self, client_data: Dict[str, Any]) -> bool:
        """Create a new client record."""
        try:
            # Ensure required fields are present
            required_fields = ["ID", "Name"]
            for field in required_fields:
                if not client_data.get(field):
                    return False
            
            # Set record type
            client_data["Type"] = "Client"
            
            # Add to records
            self.records["Client"].append(client_data)
            return self.save_records()
        except Exception as e:
            print(f"Error creating client record: {e}")
            return False
    
    def update_client(self, client_id: str, updated_data: Dict[str, Any]) -> bool:
        """Update an existing client record."""
        try:
            for i, client in enumerate(self.records["Client"]):
                if str(client.get("ID")) == str(client_id):
                    # Ensure we keep the ID and Type
                    updated_data["ID"] = client["ID"]
                    updated_data["Type"] = "Client"
                    
                    # Update the record
                    self.records["Client"][i] = updated_data
                    return self.save_records()
            return False
        except Exception as e:
            print(f"Error updating client record: {e}")
            return False
    
    def delete_client(self, client_id: str) -> bool:
        """Delete a client record."""
        try:
            for i, client in enumerate(self.records["Client"]):
                if str(client.get("ID")) == str(client_id):
                    # Remove the record
                    self.records["Client"].pop(i)
                    return self.save_records()
            return False
        except Exception as e:
            print(f"Error deleting client record: {e}")
            return False
    
    def search_clients(self, search_term: str) -> List[Dict[str, Any]]:
        """Search for client records."""
        try:
            results = []
            search_term = search_term.lower()
            
            for client in self.records["Client"]:
                for field, value in client.items():
                    if search_term in str(value).lower():
                        results.append(client)
                        break
            
            return results
        except Exception as e:
            print(f"Error searching client records: {e}")
            return []
    
    def get_all_clients(self) -> List[Dict[str, Any]]:
        """Get all client records."""
        return self.records["Client"]
    
    def get_client_by_id(self, client_id: str) -> Optional[Dict[str, Any]]:
        """Get a client record by ID."""
        for client in self.records["Client"]:
            if str(client.get("ID")) == str(client_id):
                return client
        return None


class AirlineModel(RecordModel):
    """Model for Airline records."""
    
    def create_airline(self, airline_data: Dict[str, Any]) -> bool:
        """Create a new airline record."""
        try:
            # Ensure required fields are present
            required_fields = ["ID", "Company Name"]
            for field in required_fields:
                if not airline_data.get(field):
                    return False
            
            # Set record type
            airline_data["Type"] = "Airline"
            
            # Add to records
            self.records["Airline"].append(airline_data)
            return self.save_records()
        except Exception as e:
            print(f"Error creating airline record: {e}")
            return False
    
    def update_airline(self, airline_id: str, updated_data: Dict[str, Any]) -> bool:
        """Update an existing airline record."""
        try:
            for i, airline in enumerate(self.records["Airline"]):
                if str(airline.get("ID")) == str(airline_id):
                    # Ensure we keep the ID and Type
                    updated_data["ID"] = airline["ID"]
                    updated_data["Type"] = "Airline"
                    
                    # Update the record
                    self.records["Airline"][i] = updated_data
                    return self.save_records()
            return False
        except Exception as e:
            print(f"Error updating airline record: {e}")
            return False
    
    def delete_airline(self, airline_id: str) -> bool:
        """Delete an airline record."""
        try:
            for i, airline in enumerate(self.records["Airline"]):
                if str(airline.get("ID")) == str(airline_id):
                    # Remove the record
                    self.records["Airline"].pop(i)
                    return self.save_records()
            return False
        except Exception as e:
            print(f"Error deleting airline record: {e}")
            return False
    
    def search_airlines(self, search_term: str) -> List[Dict[str, Any]]:
        """Search for airline records."""
        try:
            results = []
            search_term = search_term.lower()
            
            for airline in self.records["Airline"]:
                for field, value in airline.items():
                    if search_term in str(value).lower():
                        results.append(airline)
                        break
            
            return results
        except Exception as e:
            print(f"Error searching airline records: {e}")
            return []
    
    def get_all_airlines(self) -> List[Dict[str, Any]]:
        """Get all airline records."""
        return self.records["Airline"]
    
    def get_airline_by_id(self, airline_id: str) -> Optional[Dict[str, Any]]:
        """Get an airline record by ID."""
        for airline in self.records["Airline"]:
            if str(airline.get("ID")) == str(airline_id):
                return airline
        return None


class FlightModel(RecordModel):
    """Model for Flight records."""
    
    def create_flight(self, flight_data: Dict[str, Any]) -> bool:
        """Create a new flight record."""
        try:
            # Ensure required fields are present
            required_fields = ["Flight ID", "Client ID", "Airline ID", "Date", "Departure", "Arrival"]
            for field in required_fields:
                if not flight_data.get(field):
                    return False
            
            # Set default status if not provided
            if not flight_data.get("Status"):
                flight_data["Status"] = "Pending"
            
            # Add to records
            self.records["Flight"].append(flight_data)
            return self.save_records()
        except Exception as e:
            print(f"Error creating flight record: {e}")
            return False
    
    def update_flight(self, flight_id: str, updated_data: Dict[str, Any]) -> bool:
        """Update an existing flight record."""
        try:
            for i, flight in enumerate(self.records["Flight"]):
                if str(flight.get("Flight ID")) == str(flight_id):
                    # Ensure we keep the Flight ID
                    updated_data["Flight ID"] = flight["Flight ID"]
                    
                    # Update the record
                    self.records["Flight"][i] = updated_data
                    return self.save_records()
            return False
        except Exception as e:
            print(f"Error updating flight record: {e}")
            return False
    
    def delete_flight(self, flight_id: str) -> bool:
        """Delete a flight record."""
        try:
            for i, flight in enumerate(self.records["Flight"]):
                if str(flight.get("Flight ID")) == str(flight_id):
                    # Remove the record
                    self.records["Flight"].pop(i)
                    return self.save_records()
            return False
        except Exception as e:
            print(f"Error deleting flight record: {e}")
            return False
    
    def search_flights(self, search_term: str) -> List[Dict[str, Any]]:
        """Search for flight records."""
        try:
            results = []
            search_term = search_term.lower()
            
            for flight in self.records["Flight"]:
                for field, value in flight.items():
                    if search_term in str(value).lower():
                        results.append(flight)
                        break
            
            return results
        except Exception as e:
            print(f"Error searching flight records: {e}")
            return []
    
    def get_all_flights(self) -> List[Dict[str, Any]]:
        """Get all flight records."""
        return self.records["Flight"]
    
    def get_flight_by_id(self, flight_id: str) -> Optional[Dict[str, Any]]:
        """Get a flight record by ID."""
        for flight in self.records["Flight"]:
            if str(flight.get("Flight ID")) == str(flight_id):
                return flight
        return None
