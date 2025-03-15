# Flight Record Management System - Backend Implementation Guide

## Overview
This document provides comprehensive instructions for implementing the backend functionality of the Flight Record Management System. The system is designed to manage client records, airline records, and flight bookings for a specialist travel agent, following the Model-View-Controller (MVC) architecture pattern.

## Architecture 

The application follows a strict MVC architecture with the following components:

- **Views** (`views.py`): Already implemented - handles all UI components and user interactions through a tkinter-based GUI
- **Controllers** (`controllers.py`): Handles business logic, validation, and mediates between views and models
- **Models** (`models.py`): Manages data storage, retrieval, and persistence

## Data Structure Requirements

### Base Record Structure
All records should be stored in a dictionary-based format and persisted as JSON files. The system will use a central JSON file with separate sections for each record type.

### Client Records
Required fields:
- ID: str (numeric string)
- Type: str (always "Client")
- Name: str (required)
- Address Line 1: str
- City: str
- State: str
- Zip Code: str
- Country: str
- Phone Number: str

### Airline Records
Required fields:
- ID: str (numeric string)
- Type: str (always "Airline")
- Company Name: str (required)
- Country: str
- IATA Code: str (2-letter code, alphabetic characters only)

### Flight Records
Required fields:
- Flight ID: str (required)
- Client ID: str (must reference a valid client)
- Airline ID: str (must reference a valid airline)
- Date: str (format: YYYY-MM-DD)
- Departure: str (departure city, required)
- Arrival: str (arrival city, required)
- Status: str (defaults to "Pending" if not provided)

## Backend Implementation Requirements

### 1. Base Record Model
Implement a `RecordModel` class with common functionality:
- Loading records from JSON file
- Saving records to JSON file
- Basic error handling
- Initializing with default empty structure if file doesn't exist

### 2. Specific Model Classes
Extend the base `RecordModel` class for each record type:

#### ClientModel
- Create client records with validation
- Update client records
- Delete client records
- Search client records by any field
- Retrieve all clients
- Retrieve client by ID

#### AirlineModel
- Create airline records with validation
- Update airline records
- Delete airline records
- Search airline records by any field
- Retrieve all airlines
- Retrieve airline by ID

#### FlightModel
- Create flight records with validation
- Update flight records
- Delete flight records
- Search flight records by any field
- Retrieve all flights
- Retrieve flight by ID

### 3. Controller Classes
Implement controller classes as interfaces between the views and models:

#### ClientController
```python
def __init__(self, model: ClientModel, view_update_callback: Optional[Callable] = None):
    """Initialize with model and optional view update callback."""
    
def create_client(self, client_data: Dict[str, Any]) -> bool:
    """Create a new client record with validation."""
    
def update_client(self, client_id: str, updated_data: Dict[str, Any]) -> bool:
    """Update an existing client record."""
    
def delete_client(self, client_id: str) -> bool:
    """Delete a client record."""
    
def search_clients(self, search_term: str) -> List[Dict[str, Any]]:
    """Search for client records by term."""
    
def get_all_clients(self) -> List[Dict[str, Any]]:
    """Get all client records."""
    
def get_client_by_id(self, client_id: str) -> Optional[Dict[str, Any]]:
    """Get a client record by ID."""
    
def _validate_client_data(self, client_data: Dict[str, Any]) -> bool:
    """Validate client data before creating or updating."""
```

#### AirlineController
```python
def __init__(self, model: AirlineModel, view_update_callback: Optional[Callable] = None):
    """Initialize with model and optional view update callback."""
    
def create_airline(self, airline_data: Dict[str, Any]) -> bool:
    """Create a new airline record with validation."""
    
def update_airline(self, airline_id: str, updated_data: Dict[str, Any]) -> bool:
    """Update an existing airline record."""
    
def delete_airline(self, airline_id: str) -> bool:
    """Delete an airline record."""
    
def search_airlines(self, search_term: str) -> List[Dict[str, Any]]:
    """Search for airline records by term."""
    
def get_all_airlines(self) -> List[Dict[str, Any]]:
    """Get all airline records."""
    
def get_airline_by_id(self, airline_id: str) -> Optional[Dict[str, Any]]:
    """Get an airline record by ID."""
    
def _validate_airline_data(self, airline_data: Dict[str, Any]) -> bool:
    """Validate airline data before creating or updating."""
```

#### FlightController
```python
def __init__(self, model: FlightModel, view_update_callback: Optional[Callable] = None):
    """Initialize with model and optional view update callback."""
    
def create_flight(self, flight_data: Dict[str, Any]) -> bool:
    """Create a new flight record with validation."""
    
def update_flight(self, flight_id: str, updated_data: Dict[str, Any]) -> bool:
    """Update an existing flight record."""
    
def delete_flight(self, flight_id: str) -> bool:
    """Delete a flight record."""
    
def search_flights(self, search_term: str) -> List[Dict[str, Any]]:
    """Search for flight records by term."""
    
def get_all_flights(self) -> List[Dict[str, Any]]:
    """Get all flight records."""
    
def get_flight_by_id(self, flight_id: str) -> Optional[Dict[str, Any]]:
    """Get a flight record by ID."""
    
def _validate_flight_data(self, flight_data: Dict[str, Any]) -> bool:
    """Validate flight data before creating or updating."""
```

## 4. Validation Requirements

### Client Data Validation
- Name must be provided
- ID must be numeric if provided
- Add more validation as needed

### Airline Data Validation
- Company Name must be provided
- ID must be numeric if provided
- IATA Code must be exactly 2 alphabetic characters if provided
- Add more validation as needed

### Flight Data Validation
- All required fields must be present (Flight ID, Client ID, Airline ID, Date, Departure, Arrival)
- Date format must be valid (YYYY-MM-DD)
- Client ID and Airline ID should reference existing records (referential integrity)

## 5. Error Handling

Implement robust error handling throughout the backend:
- Catch and log exceptions
- Return meaningful error messages
- Prevent data corruption
- Handle file I/O errors gracefully

## 6. Data Persistence

### JSON File Format
The application should use a central JSON file with the following structure:
```json
{
    "Client": [
        {
            "ID": "1",
            "Type": "Client",
            "Name": "John Doe",
            "Address Line 1": "123 Main St",
            "City": "London",
            "State": "Greater London",
            "Country": "UK",
            "Phone Number": "0123456789"
        }
    ],
    "Airline": [
        {
            "ID": "101",
            "Type": "Airline",
            "Company Name": "Global Airlines",
            "Country": "USA",
            "IATA Code": "GA"
        }
    ],
    "Flight": [
        {
            "Flight ID": "F001",
            "Client ID": "1",
            "Airline ID": "101",
            "Date": "2025-03-05",
            "Departure": "London",
            "Arrival": "Paris",
            "Status": "Confirmed"
        }
    ]
}
```

### File Operations
- Check for existing file on startup
- Create a default structure if no file exists
- Save changes immediately after modifications
- Handle file locking for concurrent access (if needed)

## 7. Testing Requirements

### Unit Testing
Implement comprehensive unit tests for all backend components:

#### Model Tests
- Test loading records from file
- Test saving records to file
- Test CRUD operations for each record type
- Test search functionality
- Test validation logic

#### Controller Tests
- Test validation logic
- Test interaction with models
- Test callbacks to views
- Test error handling

### Integration Testing
- Test the complete workflow from controller to model
- Test data persistence
- Test referential integrity

## Implementation Guide

1. Start by implementing the base RecordModel class with file operations
2. Implement specific model classes with their CRUD operations
3. Implement controller classes with validation logic
4. Set up proper error handling and logging
5. Write unit tests for all components
6. Ensure data persistence works correctly
7. Integrate with the existing view components

## Notes for Integration with Frontend

- The frontend expects controllers to return boolean values for operation success
- Search operations should return matching records as a list
- Error messages should be handled by the controllers
- The view has callbacks for refreshing displays after operations
- The application initializes controllers and models in the main.py file

By following these guidelines, you will create a robust backend system that integrates seamlessly with the existing frontend components to deliver a complete Flight Record Management System.