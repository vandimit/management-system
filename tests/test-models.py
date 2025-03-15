import unittest
import os
import json
import tempfile
from src.models import ClientModel, AirlineModel, FlightModel


class TestClientModel(unittest.TestCase):
    """Test case for the ClientModel class."""
    
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
        self.temp_file.close()
        
        # Initialize test data
        test_data = {
            "Client": [
                {
                    "ID": "1",
                    "Type": "Regular",
                    "Name": "John Doe",
                    "Address Line 1": "123 Main St",
                    "City": "London",
                    "State": "Greater London",
                    "Country": "UK",
                    "Phone Number": "0123456789"
                }
            ],
            "Airline": [],
            "Flight": []
        }
        
        # Write test data to file
        with open(self.temp_file.name, 'w') as f:
            json.dump(test_data, f)
        
        # Initialize model with test file
        self.model = ClientModel(self.temp_file.name)
    
    def tearDown(self):
        # Remove temporary file
        os.unlink(self.temp_file.name)
    
    def test_load_records(self):
        """Test loading records from file."""
        records = self.model.records
        self.assertIn("Client", records)
        self.assertEqual(len(records["Client"]), 1)
        self.assertEqual(records["Client"][0]["Name"], "John Doe")
    
    def test_create_client(self):
        """Test creating a new client record."""
        new_client = {
            "ID": "2",
            "Name": "Jane Smith",
            "Address Line 1": "456 Side Ave",
            "City": "Manchester",
            "Country": "UK",
            "Phone Number": "0987654321"
        }
        
        result = self.model.create_client(new_client)
        self.assertTrue(result)
        
        # Verify client was added
        self.assertEqual(len(self.model.records["Client"]), 2)
        self.assertEqual(self.model.records["Client"][1]["Name"], "Jane Smith")
        
        # Verify file was updated
        with open(self.temp_file.name, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data["Client"]), 2)
            self.assertEqual(data["Client"][1]["Name"], "Jane Smith")
    
    def test_update_client(self):
        """Test updating an existing client record."""
        updated_data = {
            "Name": "John Doe Updated",
            "Address Line 1": "123 Main St",
            "City": "London",
            "State": "Greater London",
            "Country": "UK",
            "Phone Number": "0123456789"
        }
        
        result = self.model.update_client("1", updated_data)
        self.assertTrue(result)
        
        # Verify client was updated
        self.assertEqual(self.model.records["Client"][0]["Name"], "John Doe Updated")
        
        # Verify file was updated
        with open(self.temp_file.name, 'r') as f:
            data = json.load(f)
            self.assertEqual(data["Client"][0]["Name"], "John Doe Updated")
    
    def test_delete_client(self):
        """Test deleting a client record."""
        result = self.model.delete_client("1")
        self.assertTrue(result)
        
        # Verify client was deleted
        self.assertEqual(len(self.model.records["Client"]), 0)
        
        # Verify file was updated
        with open(self.temp_file.name, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data["Client"]), 0)
    
    def test_search_clients(self):
        """Test searching for clients."""
        # Add another client
        self.model.create_client({
            "ID": "2",
            "Type": "Premium",
            "Name": "Alice Johnson",
            "Country": "USA"
        })
        
        # Search by name
        results = self.model.search_clients("John")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["Name"], "John Doe")
        
        # Search by country
        results = self.model.search_clients("UK")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["Country"], "UK")
        
        # Search that should return multiple results
        results = self.model.search_clients("o")  # Matches "John Doe" and "London"
        self.assertEqual(len(results), 1)  # Should find 1 client (with "John" and "London")
    
    def test_get_client_by_id(self):
        """Test retrieving a client by ID."""
        client = self.model.get_client_by_id("1")
        self.assertIsNotNone(client)
        self.assertEqual(client["Name"], "John Doe")
        
        # Test non-existent ID
        client = self.model.get_client_by_id("999")
        self.assertIsNone(client)


class TestAirlineModel(unittest.TestCase):
    """Test case for the AirlineModel class."""
    
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
        self.temp_file.close()
        
        # Initialize test data
        test_data = {
            "Client": [],
            "Airline": [
                {
                    "ID": "101",
                    "Type": "International",
                    "Company Name": "Global Airlines",
                    "Country": "USA",
                    "IATA Code": "GA"
                }
            ],
            "Flight": []
        }
        
        # Write test data to file
        with open(self.temp_file.name, 'w') as f:
            json.dump(test_data, f)
        
        # Initialize model with test file
        self.model = AirlineModel(self.temp_file.name)
    
    def tearDown(self):
        # Remove temporary file
        os.unlink(self.temp_file.name)
    
    # Additional test methods for AirlineModel would go here
    # Similar to TestClientModel but with airline-specific operations


class TestFlightModel(unittest.TestCase):
    """Test case for the FlightModel class."""
    
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
        self.temp_file.close()
        
        # Initialize test data
        test_data = {
            "Client": [],
            "Airline": [],
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
        
        # Write test data to file
        with open(self.temp_file.name, 'w') as f:
            json.dump(test_data, f)
        
        # Initialize model with test file
        self.model = FlightModel(self.temp_file.name)
    
    def tearDown(self):
        # Remove temporary file
        os.unlink(self.temp_file.name)
    
    # Additional test methods for FlightModel would go here
    # Similar to TestClientModel but with flight-specific operations


if __name__ == '__main__':
    unittest.main()
