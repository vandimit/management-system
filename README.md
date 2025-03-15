# Flight Record Management System

## Overview

The Flight Record Management System is a specialized application for travel agencies to manage client records, airline information, and flight bookings. This system provides a comprehensive solution for creating, updating, searching, and displaying travel-related records through an intuitive graphical interface.

## Architecture

The application follows the Model-View-Controller (MVC) architectural pattern with a clean separation between frontend and backend components:

- **Model**: Handles data storage, retrieval, validation, and business logic
- **View**: Manages the user interface and user interactions
- **Controller**: Processes user actions and coordinates between model and view

### Backend Components

The backend implementation focuses on robust data management:

- **FileOperations**: Handles file I/O operations for record persistence
- **DataValidator**: Validates data integrity and enforces business rules
- **RecordManager**: Base class for record operations
- **ClientManager**: Manages client-related operations
- **AirlineManager**: Manages airline-related operations
- **FlightManager**: Manages flight-related operations

### Frontend-Backend Integration

The integration layer connects the frontend UI with the backend functionality:

- **ClientController**: Processes client-related user actions
- **AirlineController**: Processes airline-related user actions
- **FlightController**: Processes flight-related user actions

## Features

- **Client Management**: Create and maintain client profiles
- **Airline Management**: Track airline companies and their information
- **Flight Management**: Book and manage flight records
- **Data Validation**: Robust validation of all record fields
- **Referential Integrity**: Ensures consistency between related records
- **Search Functionality**: Find records based on various criteria
- **Modern UI**: Intuitive interface with tabbed organization
- **Data Persistence**: All records are stored in JSON format

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/flight-record-management.git
   cd flight-record-management
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## File Structure

```
.
├── README.md
├── requirements.txt
├── src
│   ├── backend_implementation.py   # Backend components
│   ├── frontend_backend_integration.py  # Integration layer
│   ├── main.py                     # Application entry point
│   ├── views.py                    # UI components
│   └── data/                       # Data storage directory
│       ├── clients.json
│       ├── airlines.json
│       └── flights.json
└── tests
    ├── test_backend.py
    ├── test_integration.py
    └── test_views.py
```

## Data Models

### Client Record
- **ID**: int (Unique identifier)
- **Type**: str (Type of record - "Client")
- **Name**: str (Client's full name)
- **Address Line 1**: str (Primary address line)
- **Address Line 2**: str (Secondary address line - optional)
- **Address Line 3**: str (Tertiary address line - optional)
- **City**: str (City name)
- **State**: str (State/province)
- **Zip Code**: str (Postal/zip code)
- **Country**: str (Country name)
- **Phone Number**: str (Contact telephone number)

### Airline Record
- **ID**: int (Unique identifier)
- **Type**: str (Type of record - "Airline")
- **Company Name**: str (Airline company name)
- **Country**: str (Country of registration - optional)
- **IATA Code**: str (IATA identifier code - optional)

### Flight Record
- **Flight ID**: int (Unique identifier)
- **Client_ID**: int (Foreign key to Client record)
- **Airline_ID**: int (Foreign key to Airline record)
- **Date**: str (Date of flight in YYYY-MM-DD format)
- **Start City**: str (Departure city)
- **End City**: str (Arrival city)
- **Status**: str (Flight status - optional)

## Usage

### Client Management

1. **Creating a Client**:
   - Navigate to the "Clients" tab
   - Fill in the client details form
   - Click the "Create" button

2. **Updating a Client**:
   - Select an existing client from the list
   - Modify the details in the form
   - Click the "Update" button

3. **Deleting a Client**:
   - Select an existing client from the list
   - Click the "Delete" button
   - Confirm the deletion when prompted

4. **Searching for Clients**:
   - Click the "Search" button
   - Enter search criteria
   - View results in the client list

### Airline Management

Similar operations are available in the "Airlines" tab for managing airline records.

### Flight Management

The "Flights" tab provides functionality for managing flight bookings, including creating, updating, deleting, and searching for flights.

## Data Storage

Records are stored in JSON files in the following format:

```json
// clients.json
[
  {
    "ID": 1,
    "Type": "Client",
    "Name": "John Doe",
    "Address Line 1": "123 Main St",
    "City": "London",
    "State": "Greater London",
    "Country": "UK",
    "Phone Number": "0123456789"
  }
]

// airlines.json
[
  {
    "ID": 101,
    "Type": "Airline",
    "Company Name": "Global Airways",
    "Country": "USA",
    "IATA Code": "GA"
  }
]

// flights.json
[
  {
    "Flight ID": 1,
    "Client_ID": 1,
    "Airline_ID": 101,
    "Date": "2025-03-05",
    "Start City": "London",
    "End City": "Paris",
    "Status": "Confirmed"
  }
]
```

## Testing

Run the test suite to verify the functionality of the application:

```
python -m unittest discover tests
```

## Error Handling

The application includes comprehensive error handling:

- **Data Validation**: Input is validated before processing
- **File Operations**: Errors during file I/O operations are caught and handled
- **User Feedback**: Clear error messages are displayed to the user

## Development Guidelines

When contributing to this project:

1. Follow the MVC architecture
2. Validate all input data
3. Maintain separation of concerns
4. Add appropriate error handling
5. Write unit tests for new functionality
6. Follow PEP 8 style guidelines
7. Document code with clear docstrings

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributors

- Your Name - Initial work