import unittest
from unittest.mock import MagicMock, patch
from src.controllers import ClientController, AirlineController, FlightController


class TestClientController(unittest.TestCase):
    """Test case for the ClientController class."""
    
    def setUp(self):
        # Create mock model
        self.mock_model = MagicMock()
        
        # Create mock view callback
        self.mock_callback = MagicMock()
        
        # Create controller with mocks
        self.controller = ClientController(self.mock_model, self.mock_callback)
    
    def test_create_client_valid(self):
        """Test creating a client with valid data."""
        # Set up test data
        client_data = {
            "ID": "1",
            "Name": "John Doe",
            "Address Line 1": "123 Main St",
            "City": "London",
            "Country": "UK"
        }
        
        # Set up mock model behavior
        self.mock_model.create_client.return_value = True
        
        # Call controller method
        result = self.controller.create_client(client_data)
        
        # Verify model was called with correct data
        self.mock_model.create_client.assert_called_once_with(client_data)
        
        # Verify result
        self.assertTrue(result)
        
        # Verify callback was called
        self.mock_callback.assert_called_once()
    
    def test_create_client_invalid(self):
        """Test creating a client with invalid data."""
        # Set up test data with missing required field
        client_data = {
            "ID": "1",
            "Name": ""  # Empty name, should be invalid
        }
        
        # Call controller method
        result = self.controller.create_client(client_data)
        
        # Verify model was not called
        self.mock_model.create_client.assert_not_called()
        
        # Verify result
        self.assertFalse(result)
        
        # Verify callback was not called
        self.mock_callback.assert_not_called()
    
    def test_update_client_valid(self):
        """Test updating a client with valid data."""
        # Set up test data
        client_id = "1"
        updated_data = {
            "Name": "John Doe Updated",
            "Address Line 1": "123 Main St",
            "City": "London",
            "Country": "UK"
        }
        
        # Set up mock model behavior
        self.mock_model.update_client.return_value = True
        
        # Call controller method
        result = self.controller.update_client(client_id, updated_data)
        
        # Verify model was called with correct data
        self.mock_model.update_client.assert_called_once_with(client_id, updated_data)
        
        # Verify result
        self.assertTrue(result)
        
        # Verify callback was called
        self.mock_callback.assert_called_once()
    
    def test_update_client_invalid(self):
        """Test updating a client with invalid data."""
        # Set up test data with missing required field
        client_id = "1"
        updated_data = {
            "Name": ""  # Empty name, should be invalid
        }
        
        # Call controller method
        result = self.controller.update_client(client_id, updated_data)
        
        # Verify model was not called
        self.mock_model.update_client.assert_not_called()
        
        # Verify result
        self.assertFalse(result)
        
        # Verify callback was not called
        self.mock_callback.assert_not_called()
    
    def test_delete_client(self):
        """Test deleting a client."""
        # Set up test data
        client_id = "1"
        
        # Set up mock model behavior
        self.mock_model.delete_client.return_value = True
        
        # Call controller method
        result = self.controller.delete_client(client_id)
        
        # Verify model was called with correct data
        self.mock_model.delete_client.assert_called_once_with(client_id)
        
        # Verify result
        self.assertTrue(result)
        
        # Verify callback was called
        self.mock_callback.assert_called_once()
    
    def test_search_clients(self):
        """Test searching for clients."""
        # Set up test data
        search_term = "John"
        mock_results = [
            {"ID": "1", "Name": "John Doe", "Country": "UK"}
        ]
        
        # Set up mock model behavior
        self.mock_model.search_clients.return_value = mock_results
        
        # Call controller method
        results = self.controller.search_clients(search_term)
        
        # Verify model was called with correct data
        self.mock_model.search_clients.assert_called_once_with(search_term)
        
        # Verify results
        self.assertEqual(results, mock_results)
    
    def test_get_all_clients(self):
        """Test getting all clients."""
        # Set up mock model behavior
        mock_clients = [
            {"ID": "1", "Name": "John Doe", "Country": "UK"},
            {"ID": "2", "Name": "Jane Smith", "Country": "USA"}
        ]
        self.mock_model.get_all_clients.return_value = mock_clients
        
        # Call controller method
        results = self.controller.get_all_clients()
        
        # Verify model was called
        self.mock_model.get_all_clients.assert_called_once()
        
        # Verify results
        self.assertEqual(results, mock_clients)
    
    def test_get_client_by_id(self):
        """Test getting a client by ID."""
        # Set up test data
        client_id = "1"
        mock_client = {"ID": "1", "Name": "John Doe", "Country": "UK"}
        
        # Set up mock model behavior
        self.mock_model.get_client_by_id.return_value = mock_client
        
        # Call controller method
        result = self.controller.get_client_by_id(client_id)
        
        # Verify model was called with correct data
        self.mock_model.get_client_by_id.assert_called_once_with(client_id)
        
        # Verify result
        self.assertEqual(result, mock_client)


class TestAirlineController(unittest.TestCase):
    """Test case for the AirlineController class."""
    
    def setUp(self):
        # Create mock model
        self.mock_model = MagicMock()
        
        # Create mock view callback
        self.mock_callback = MagicMock()
        
        # Create controller with mocks
        self.controller = AirlineController(self.mock_model, self.mock_callback)
    
    # Additional test methods for AirlineController would go here
    # Similar to TestClientController but with airline-specific operations


class TestFlightController(unittest.TestCase):
    """Test case for the FlightController class."""
    
    def setUp(self):
        # Create mock model
        self.mock_model = MagicMock()
        
        # Create mock view callback
        self.mock_callback = MagicMock()
        
        # Create controller with mocks
        self.controller = FlightController(self.mock_model, self.mock_callback)
    
    # Additional test methods for FlightController would go here
    # Similar to TestClientController but with flight-specific operations


if __name__ == '__main__':
    unittest.main()
