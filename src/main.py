#!/usr/bin/env python3
"""
Flight Record Management System
Main Application Entry Point

This module initializes the MVC architecture for the Flight Record Management System
and launches the application.
"""

import os
import sys
from tkinter import messagebox

from pkg.json_db import JsonFileDB
from src.airline.repository_json import AirlineRepositoryJson
from src.client.controller import ClientController
from src.airline.controller import AirlineController
from src.client.repository_json import ClientRepositoryJson
from src.flight.controller import FlightController
from src.flight.repository_json import FlightRepositoryJson
from views import RecordManagementGUI


def main():
    """Initialize the application and start the main event loop."""
    try:
        # Set up data file path
        data_dir = os.path.join(os.path.dirname(__file__), "data")
        os.makedirs(data_dir, exist_ok=True)
        data_file = os.path.join(data_dir, "records.json")

        # Initialize JSON database with data file
        json_db = JsonFileDB(data_file)

        # Initialize models (repositories) with the JSON database
        client_repository = ClientRepositoryJson(json_db)
        airline_repository = AirlineRepositoryJson(json_db)
        flight_repository = FlightRepositoryJson(json_db)

        # Create GUI instance first (without showing it)
        app = RecordManagementGUI()

        # Set up controllers with view update callbacks
        client_controller = ClientController(
            client_repository=client_repository,
            view_update_callback=app.display_client_records
        )
        airline_controller = AirlineController(
            airline_repository=airline_repository,
            view_update_callback=app.display_airline_records
        )
        flight_controller = FlightController(
            flight_repository=flight_repository,
            view_update_callback=app.display_flight_records
        )

        # Inject controllers into the view
        app.client_controller = client_controller
        app.airline_controller = airline_controller
        app.flight_controller = flight_controller

        # Refresh all displays
        app.display_client_records()
        app.display_airline_records()
        app.display_flight_records()

        # Start the main event loop
        app.mainloop()
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while starting the application: {str(e)}")
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
