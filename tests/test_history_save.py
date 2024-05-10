'''Tests for the SaveHistoryCommand class.'''
from unittest.mock import patch
from app.plugins.history.save import SaveHistoryCommand
from app.calculation_history import CalculationHistory

# Assuming CalculationHistory is a singleton or similarly accessible instance
@patch.object(CalculationHistory, 'save_history')
def test_save_history_success(mock_save_history):
    '''Test saving history successfully.'''
    # Create an instance of SaveHistoryCommand and execute
    command = SaveHistoryCommand()
    command.execute()

    # Assertions
    mock_save_history.assert_called_once()

@patch.object(CalculationHistory, 'save_history', side_effect=Exception("Permission denied"))
@patch('logging.error')
def test_save_history_failure(mock_logging_error, mock_save_history):
    '''Test handling errors during history saving (e.g., permission issues).'''
    command = SaveHistoryCommand()

    # In the actual implementation, you might handle exceptions to log errors,
    # so here we're checking if an error log is produced when an exception is raised.
    command.execute()

    # Assertions
    mock_save_history.assert_called_once()
    mock_logging_error.assert_called_once_with("Failed to save history due to: Permission denied")
