# Front-End Back-End Integration Specification
# Flight Record Management System

## 1. Introduction

### 1.1 Purpose
This document defines the integration specifications between the frontend and backend components of the Flight Record Management System designed for specialist travel agents. It outlines the data flow, communication protocols, and interfaces necessary for seamless operation of the application.

### 1.2 Scope
This specification covers:
- Data structures for client, airline, and flight records
- API endpoints and communication methods
- Validation requirements
- Error handling protocols
- Integration testing parameters

### 1.3 System Overview
The Flight Record Management System follows the Model-View-Controller (MVC) architectural pattern:
- **Frontend**: The View component implemented with Tkinter, providing the graphical user interface
- **Backend**: The Model component responsible for data storage, retrieval, and business logic
- **Controllers**: Components that coordinate interactions between frontend and backend

## 2. Architecture Overview

### 2.1 Component Diagram
```
┌───────────────────────┐      ┌───────────────────────┐
│                       │      │                       │
│       Frontend        │◄────►│      Controllers      │
│   (User Interface)    │      │    (Coordination)     │
│                       │      │                       │
└───────────────────────┘      └─────────┬─────────────┘
                                         │
                                         ▼
                               ┌───────────────────────┐
                               │                       │
                               │       Backend         │
                               │    (Data & Logic)     │
                               │                       │
                               └───────────────────────┘
```

### 2.2 Communication Flow
1. User interacts with the Frontend (View)
2. View notifies Controller of user action
3. Controller processes the action and calls appropriate Backend (Model) methods
4. Backend performs operations and returns results to Controller
5. Controller updates the View with results
6. View displays updated information to the user

### 2.3 Technology Stack
- **Frontend**: Python Tkinter
- **Backend**: Python with JSON file storage
- **Communication**: Direct method calls (in-process)

## 3. Data Models

### 3.1 Client Record
```json
{
  "ID": "int (unique identifier)",
  "Type": "str ('Client')",
  "Name": "str (required)",
  "Address Line 1": "str",
  "Address Line 2": "str (optional)",
  "Address Line 3": "str (optional)",
  "City": "str",
  "State": "str",
  "Zip Code": "str",
  "Country": "str",
  "Phone Number": "str"
}
```

### 3.2 Airline Record
```json
{
  "ID": "int (unique identifier)",
  "Type": "str ('Airline')",
  "Company Name": "str (required)",
  "Country": "str (optional)",
  "IATA Code": "str (optional, 2 characters)"
}
```

### 3.3 Flight Record
```json
{
  "Flight ID": "int (unique identifier)",
  "Client_ID": "int (foreign key to Client)",
  "Airline_ID": "int (foreign key to Airline)",
  "Date": "str (YYYY-MM-DD format)",
  "Start City": "str (required)",
  "End City": "str (required)",
  "Status": "str (optional)"
}
```

## 4. Frontend-Backend Interface

### 4.1 Controller Interfaces

#### 4.1.1 ClientController
```python
class ClientController:
    def __init__(self, view_update_callback=None)
    def create_client(self, client_data: Dict[str, Any]) -> bool
    def update_client(self, client_id: str, updated_data: Dict[str, Any]) -> bool
    def delete_client(self, client_id: str) -> bool
    def search_clients(self, search_term: str) -> List[Dict[str, Any]]
    def get_all_clients(self) -> List[Dict[str, Any]]
    def get_client_by_id(self, client_id: str) -> Optional[Dict[str, Any]]
```

#### 4.1.2 AirlineController
```python
class AirlineController:
    def __init__(self, view_update_callback=None)
    def create_airline(self, airline_data: Dict[str, Any]) -> bool
    def update_airline(self, airline_id: str, updated_data: Dict[str, Any]) -> bool
    def delete_airline(self, airline_id: str) -> bool
    def search_airlines(self, search_term: str) -> List[Dict[str, Any]]
    def get_all_airlines(self) -> List[Dict[str, Any]]
    def get_airline_by_id(self, airline_id: str) -> Optional[Dict[str, Any]]
```

#### 4.1.3 FlightController
```python
class FlightController:
    def __init__(self, view_update_callback=None)
    def create_flight(self, flight_data: Dict[str, Any]) -> bool
    def update_flight(self, flight_id: str, updated_data: Dict[str, Any]) -> bool
    def delete_flight(self, flight_id: str) -> bool
    def search_flights(self, search_term: str) -> List[Dict[str, Any]]
    def get_all_flights(self) -> List[Dict[str, Any]]
    def get_flight_by_id(self, flight_id: str) -> Optional[Dict[str, Any]]
```

### 4.2 Backend Interfaces

#### 4.2.1 FileOperations
```python
class FileOperations:
    @staticmethod
    def check_record_files() -> Dict[str, bool]
    @staticmethod
    def load_records() -> Dict[str, List[Dict[str, Any]]]
    @staticmethod
    def save_records(records: Dict[str, List[Dict[str, Any]]]) -> bool
```

#### 4.2.2 DataValidator
```python
class DataValidator:
    @staticmethod
    def validate_client(client_data: Dict[str, Any], all_records: Dict[str, List[Dict[str, Any]]], updating_id: Optional[int] = None) -> Dict[str, Union[bool, str]]
    @staticmethod
    def validate_airline(airline_data: Dict[str, Any], all_records: Dict[str, List[Dict[str, Any]]], updating_id: Optional[int] = None) -> Dict[str, Union[bool, str]]
    @staticmethod
    def validate_flight(flight_data: Dict[str, Any], all_records: Dict[str, List[Dict[str, Any]]], updating_id: Optional[int] = None) -> Dict[str, Union[bool, str]]
```

#### 4.2.3 Record Managers
```python
class ClientManager:
    def create_client(self, client_data: Dict[str, Any]) -> Dict[str, Union[bool, Any]]
    def get_client(self, client_id: int) -> Dict[str, Union[bool, Any]]
    def update_client(self, client_id: int, client_data: Dict[str, Any]) -> Dict[str, Union[bool, Any]]
    def delete_client(self, client_id: int) -> Dict[str, Union[bool, str]]
    def search_clients(self, criteria: Dict[str, Any]) -> Dict[str, Union[bool, List[Dict[str, Any]]]]

class AirlineManager:
    def create_airline(self, airline_data: Dict[str, Any]) -> Dict[str, Union[bool, Any]]
    def get_airline(self, airline_id: int) -> Dict[str, Union[bool, Any]]
    def update_airline(self, airline_id: int, airline_data: Dict[str, Any]) -> Dict[str, Union[bool, Any]]
    def delete_airline(self, airline_id: int) -> Dict[str, Union[bool, str]]
    def search_airlines(self, criteria: Dict[str, Any]) -> Dict[str, Union[bool, List[Dict[str, Any]]]]

class FlightManager:
    def create_flight(self, flight_data: Dict[str, Any]) -> Dict[str, Union[bool, Any]]
    def get_flight(self, flight_id: int) -> Dict[str, Union[bool, Any]]
    def update_flight(self, flight_id: int, flight_data: Dict[str, Any]) -> Dict[str, Union[bool, Any]]
    def delete_flight(self, flight_id: int) -> Dict[str, Union[bool, str]]
    def search_flights(self, criteria: Dict[str, Any]) -> Dict[str, Union[bool, List[Dict[str, Any]]]]
```

## 5. Data Flow

### 5.1 Record Creation
1. User enters record data in frontend form
2. View passes data to Controller
3. Controller validates basic data format
4. Controller calls Backend create method
5. Backend validates data (including referential integrity)
6. Backend assigns ID if not provided
7. Backend saves record to storage
8. Backend returns success/failure with result or error message
9. Controller updates View based on result
10. View displays success message or error to user

### 5.2 Record Update
1. User selects existing record from list
2. View populates form with record data
3. User modifies data and submits
4. View passes data to Controller
5. Controller validates basic data format
6. Controller calls Backend update method
7. Backend validates data (including referential integrity)
8. Backend updates record in storage
9. Backend returns success/failure with result or error message
10. Controller updates View based on result
11. View displays success message or error to user

### 5.3 Record Deletion
1. User selects record to delete
2. View passes ID to Controller
3. Controller calls Backend delete method
4. Backend checks for referential integrity constraints
5. Backend removes record from storage
6. Backend returns success/failure with result or error message
7. Controller updates View based on result
8. View displays success message or error to user

### 5.4 Record Search
1. User enters search criteria
2. View passes criteria to Controller
3. Controller formats search parameters
4. Controller calls Backend search method
5. Backend performs search operation
6. Backend returns matching records
7. Controller processes records for display
8. View displays search results to user

## 6. Validation Requirements

### 6.1 Client Validation
- **ID**: Unique integer, optional for creation (auto-generated if missing)
- **Name**: Required non-empty string
- **Phone Number**: Optional, but must be valid format if provided

### 6.2 Airline Validation
- **ID**: Unique integer, optional for creation (auto-generated if missing)
- **Company Name**: Required non-empty string
- **IATA Code**: Optional, must be exactly 2 alphabetic characters if provided

### 6.3 Flight Validation
- **Flight ID**: Unique integer, optional for creation (auto-generated if missing)
- **Client_ID**: Required integer, must refer to existing client
- **Airline_ID**: Required integer, must refer to existing airline
- **Date**: Required string in YYYY-MM-DD format
- **Start City**: Required non-empty string
- **End City**: Required non-empty string

## 7. Error Handling

### 7.1 Error Types
1. **Validation Errors**: Invalid data format or missing required fields
2. **Referential Integrity Errors**: Foreign key references not found
3. **Storage Errors**: File system issues
4. **Operational Errors**: Unexpected runtime errors

### 7.2 Error Reporting
- Backend methods return structured error objects
- Controllers translate errors to user-friendly messages
- View displays appropriate error messages to users
- All errors are logged for troubleshooting

### 7.3 Error Response Format
```json
{
  "success": false,
  "error": "Descriptive error message"
}
```

## 8. Data Persistence

### 8.1 File Structure
- **clients.json**: Storage for Client records
- **airlines.json**: Storage for Airline records
- **flights.json**: Storage for Flight records

### 8.2 Storage Format
Each file contains a JSON array of record objects:
```json
[
  { /* record 1 */ },
  { /* record 2 */ },
  /* ... */
]
```

### 8.3 File Operations
- Files are created automatically if they don't exist
- All records of each type are loaded into memory at startup
- Records are saved to files after each modification
- Backup mechanism creates temporary files during save operations to prevent data loss

## 9. Integration Testing

### 9.1 Test Categories
1. **Unit Tests**: Test individual components in isolation
2. **Integration Tests**: Test interactions between components
3. **End-to-End Tests**: Test complete user workflows

### 9.2 Key Test Scenarios
- Create, read, update, and delete operations for all record types
- Validation of all data fields
- Referential integrity enforcement
- Error handling and recovery
- File I/O operations
- Search functionality with various criteria

### 9.3 Mock Components
- Frontend can be tested with mock backend components
- Backend can be tested with mock storage mechanisms
- Controllers can be tested with mock views and backends

## 10. Security Considerations

### 10.1 Data Validation
- All input data must be validated before processing
- String inputs should be sanitized to prevent injection attacks
- Integer inputs must be validated as valid numbers

### 10.2 File System Security
- File access permissions should be restricted to the application
- Files should be stored in a non-web-accessible location
- Temporary files should be securely deleted after use

### 10.3 Error Information
- Detailed error information should be logged but not exposed to users
- User-facing error messages should be generic but helpful
- System error details should not be exposed in the UI

## 11. Performance Considerations

### 11.1 Data Loading
- Records are loaded into memory at startup
- For large datasets, consider implementing pagination
- Implement lazy loading for record details

### 11.2 Search Optimization
- Implement efficient search algorithms
- Consider indexing frequently searched fields
- Optimize string comparison operations

### 11.3 UI Responsiveness
- Long-running operations should be executed in background threads
- Progress indicators should be shown for time-consuming operations
- UI should remain responsive during file operations

## 12. Implementation Guidelines

### 12.1 Code Organization
- Follow the MVC pattern strictly
- Keep frontend, backend, and controller code separate
- Use consistent naming conventions

### 12.2 Documentation
- Include docstrings for all classes and methods
- Document all parameters and return values
- Provide usage examples for complex operations

### 12.3 Error Handling
- Use try/except blocks for all file operations
- Provide meaningful error messages
- Log errors with sufficient context for debugging

## 13. Deployment Considerations

### 13.1 Dependencies
- Python 3.8 or higher
- Tkinter library
- Additional dependencies listed in requirements.txt

### 13.2 Installation
- Package application as a standalone executable
- Include README with installation instructions
- Provide setup script for first-time configuration

### 13.3 Updates
- Implement version checking mechanism
- Provide data migration for schema changes
- Ensure backward compatibility with existing data files

## 14. Glossary

- **MVC**: Model-View-Controller architectural pattern
- **Frontend**: User interface components
- **Backend**: Data storage and business logic components
- **Controller**: Coordination layer between frontend and backend
- **API**: Application Programming Interface
- **JSON**: JavaScript Object Notation, format for data storage
- **Validation**: Process of ensuring data correctness
- **Referential Integrity**: Ensuring related records exist
- **IATA Code**: International Air Transport Association identifier

## 15. Appendices

### Appendix A: Sample Data
```json
// Sample Client
{
  "ID": 1,
  "Type": "Client",
  "Name": "John Smith",
  "Address Line 1": "123 Main Street",
  "City": "London",
  "State": "Greater London",
  "Country": "UK",
  "Phone Number": "020-1234-5678"
}

// Sample Airline
{
  "ID": 101,
  "Type": "Airline",
  "Company Name": "British Airways",
  "Country": "UK",
  "IATA Code": "BA"
}

// Sample Flight
{
  "Flight ID": 1001,
  "Client_ID": 1,
  "Airline_ID": 101,
  "Date": "2025-04-15",
  "Start City": "London",
  "End City": "New York",
  "Status": "Confirmed"
}
```

### Appendix B: Error Codes and Messages
| Code | Message Template | Description |
|------|-----------------|-------------|
| V001 | "{field} is required" | Required field missing |
| V002 | "{field} must be an integer" | Invalid number format |
| V003 | "ID {id} already exists" | Duplicate identifier |
| V004 | "Invalid date format" | Date not in YYYY-MM-DD format |
| V005 | "IATA Code must be 2 alphabetic characters" | Invalid IATA format |
| R001 | "{entity} with ID {id} does not exist" | Referenced entity not found |
| R002 | "Cannot delete: {entity} has associated {related_entity}" | Deletion blocked by relationships |
| S001 | "Failed to save record" | Storage operation failed |
| S002 | "Failed to load records" | Data loading failed |

---

*Version 1.0 - Created on March 6, 2025*
