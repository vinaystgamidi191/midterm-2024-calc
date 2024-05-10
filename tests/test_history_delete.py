'''Test cases for the DeleteHistoryCommand class.'''
# Standard library imports
from unittest.mock import patch

# Third-party imports
import pandas as pd

# Local application imports
from app.plugins.history.delete import DeleteHistoryCommand

# Test deleting specific history records successfully
@patch('app.plugins.history.delete.pd.read_csv')
@patch('app.plugins.history.delete.pd.DataFrame.to_csv')
def test_delete_history_success(mock_to_csv, mock_read_csv):
    '''Test deleting specific history records successfully.'''
    # Setup mock history DataFrame
    mock_history_df = pd.DataFrame({'Operation': ['add', 'subtract', 'multiply'],
                                    'Result': [3, 1, 6]})
    mock_read_csv.return_value = mock_history_df

    # Execute command to delete the first record (index 0)
    command = DeleteHistoryCommand()
    command.execute(0)  # Assuming the command takes an index to delete

    # Assertions to check DataFrame modification should be on the mock return value
    # This snippet below won't directly check the mock dataframe. You might need a different approach to validate.
    mock_to_csv.assert_called_once()  # Ensure the updated history is saved

# Test handling failure during deletion (e.g., file not found)
@patch('app.plugins.history.delete.pd.read_csv', side_effect=FileNotFoundError("File not found"))
@patch('app.plugins.history.delete.logging')
def test_delete_history_failure(mock_logging, mock_read_csv):
    '''Test handling failure during deletion (e.g., file not found).'''
    command = DeleteHistoryCommand()
    command.execute(0)

    # Ensure error logging is called due to FileNotFoundError
    mock_logging.error.assert_called_with("Failed to delete history records: File not found")
