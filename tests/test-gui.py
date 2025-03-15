import unittest
import tkinter as tk
from unittest.mock import MagicMock, patch
from src.views import RecordManagementGUI


class TestRecordManagementGUI(unittest.TestCase):
    """Test case for the RecordManagementGUI class."""
    
    def setUp(self):
        # Create mock controllers
        self.mock_client_controller = MagicMock()
        self.mock_airline_controller = MagicMock()
        self.mock_flight_controller = MagicMock()
        
        # Set up sample data for mock controllers
        self.mock_client_controller.get_all_clients.return_value = [
            {"ID": "1", "Type": "Regular", "Name": "John Doe", "Address Line 1": "123 Main St", 
             "City": "London", "State": "Greater London", "Country": "UK", "Phone Number": "0123456789"}
        ]
        
        self.mock_airline_controller.get_all_airlines.return_value = [
            {"ID": "101", "Type": "International", "Company Name": "Global Airlines", 
             "Country": "USA", "IATA Code": "GA"}
        ]
        
        self.mock_flight_controller.get_all_flights.return_value = [
            {"Flight ID": "F001", "Client ID": "1", "Airline ID": "101", "Date": "2025-03-05",
             "Departure": "London", "Arrival": "Paris", "Status": "Confirmed"}
        ]
        
        # Initialize the GUI without running the main loop
        self.app = RecordManagementGUI(
            client_controller=self.mock_client_controller,
            airline_controller=self.mock_airline_controller,
            flight_controller=self.mock_flight_controller
        )
    
    def tearDown(self):
        # Properly destroy the GUI after tests
        self.app.destroy()
    
    def test_window_title(self):
        """Test that the window title is correct."""
        self.assertEqual(self.app.title(), "✈️ Flight Record Management System")
    
    def test_tabs_exist(self):
        """Test that all required tabs exist."""
        self.assertTrue(hasattr(self.app, 'client_frame'))
        self.assertTrue(hasattr(self.app, 'airline_frame'))
        self.assertTrue(hasattr(self.app, 'flight_frame'))
    
    def test_client_form_entries(self):
        """Test that client form has all required fields."""
        required_fields = ["ID", "Name", "Phone Number", "Country", "Address Line 1", 
                          "City", "State", "Zip Code"]
        
        for field in required_fields:
            self.assertIn(field, self.app.client_entries)
    
    def test_airline_form_entries(self):
        """Test that airline form has all required fields."""
        required_fields = ["ID", "Type", "Company Name", "Country", "IATA Code"]
        
        for field in required_fields:
            self.assertIn(field, self.app.airline_entries)
    
    def test_flight_form_entries(self):
        """Test that flight form has all required fields."""
        required_fields = ["Flight ID", "Client ID", "Airline ID", "Date", 
                          "Departure", "Arrival", "Status"]
        
        for field in required_fields:
            self.assertIn(field, self.app.flight_entries)
    
    def test_client_tree_columns(self):
        """Test that client treeview has correct columns."""
        expected_columns = ("ID", "Type", "Name", "Address Line 1", "City", 
                           "State", "Country", "Phone Number")
        
        actual_columns = self.app.client_tree["columns"]
        self.assertEqual(actual_columns, expected_columns)
    
    def test_airline_tree_columns(self):
        """Test that airline treeview has correct columns."""
        expected_columns = ("ID", "Type", "Company Name", "Country", "IATA Code")
        
        actual_columns = self.app.airline_tree["columns"]
        self.assertEqual(actual_columns, expected_columns)
    
    def test_flight_tree_columns(self):
        """Test that flight treeview has correct columns."""
        expected_columns = ("Flight ID", "Client ID", "Airline ID", "Date", 
                           "Departure", "Arrival", "Status")
        
        actual_columns = self.app.flight_tree["columns"]
        self.assertEqual(actual_columns, expected_columns)
    
    def test_client_data_loaded(self):
        """Test that client data is loaded from controller."""
        # Ensure that get_all_clients was called
        self.mock_client_controller.get_all_clients.assert_called_once()
        
        # Check that the tree has the expected number of items
        self.assertEqual(len(self.app.client_tree.get_children()), 1)
    
    def test_airline_data_loaded(self):
        """Test that airline data is loaded from controller."""
        # Ensure that get_all_airlines was called
        self.mock_airline_controller.get_all_airlines.assert_called_once()
        
        # Check that the tree has the expected number of items
        self.assertEqual(len(self.app.airline_tree.get_children()), 1)
    
    def test_flight_data_loaded(self):
        """Test that flight data is loaded from controller."""
        # Ensure that get_all_flights was called
        self.mock_flight_controller.get_all_flights.assert_called_once()
        
        # Check that the tree has the expected number of items
        self.assertEqual(len(self.app.flight_tree.get_children()), 1)
    
    @patch('src.views.messagebox')
    def test_create_client_record(self, mock_messagebox):
        """Test creating a client record."""
        # Set up form data
        self.app.client_entries["ID"].insert(0, "2")
        self.app.client_entries["Name"].insert(0, "Jane Smith")
        self.app.client_entries["Address Line 1"].insert(0, "456 Side Ave")
        self.app.client_entries["City"].insert(0, "Manchester")
        self.app.client_entries["Country"].insert(0, "UK")
        
        # Set up controller response
        self.mock_client_controller.create_client.return_value = True
        
        # Call the method
        self.app.create_client_record()
        
        # Check that controller was called with correct data
        self.mock_client_controller.create_client.assert_called_once()
        called_data = self.mock_client_controller.create_client.call_args[0][0]
        self.assertEqual(called_data["ID"], "2")
        self.assertEqual(called_data["Name"], "Jane Smith")
        
        # Check that success message was shown
        mock_messagebox.showinfo.assert_called_once_with("Success", "Client record created successfully.")


if __name__ == '__main__':
    unittest.main()
