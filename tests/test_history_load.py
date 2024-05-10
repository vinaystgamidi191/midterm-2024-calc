''' This file contains tests for the LoadHistoryCommand class in the history plugin. '''

# Standard library imports
from unittest.mock import patch

# Third-party imports
import pandas as pd

# Local application imports
from app.plugins.history.load import LoadHistoryCommand

@patch('pandas.read_csv')
@patch('logging.info')
def test_load_history_success(mock_logging_info, mock_read_csv):
    """
    Test loading history successfully. Verifies that read_csv is called correctly
    and that logging.info is called with "History Loaded".
    """
    # Setup mock DataFrame to return
    mock_df = pd.DataFrame({
        'Operation': ['add', 'subtract'],
        'Result': [3, 1]
    })
    mock_read_csv.return_value = mock_df

    # Execute command
    command = LoadHistoryCommand()
    command.execute()

    # Assertions
    mock_read_csv.assert_called_once_with("./data/calculation_history.csv")
    assert mock_logging_info.call_count == 2
    mock_logging_info.assert_called_with("History Loaded")

@patch('pandas.read_csv', side_effect=FileNotFoundError)
@patch('logging.error')
def test_load_history_failure(mock_logging_error, mock_read_csv):
    """
    Test handling errors during history loading (e.g., file not found).
    Verifies that read_csv is called correctly and that logging.error is
    called with "Parsing data error".
    """
    command = LoadHistoryCommand()
    command.execute()

    # Assertions
    mock_read_csv.assert_called_once_with("./data/calculation_history.csv")
    mock_logging_error.assert_called_once_with("Parsing data error")
