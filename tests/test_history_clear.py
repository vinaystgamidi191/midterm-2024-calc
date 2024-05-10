''' This file contains the tests for the clear command in the history plugin. '''
from unittest.mock import patch, mock_open
from app.plugins.history.clear import ClearCommand

@patch('pandas.DataFrame.to_csv')
@patch('logging.info')
@patch("builtins.open", new_callable=mock_open, read_data="data")
def test_clear_history(mock_file, mock_logging_info, mock_to_csv):
    ''' Test clearing history successfully.'''
    # Execute the clear command
    command = ClearCommand()
    command.execute()

    # Check that the file was opened in write mode and truncated
    mock_file.assert_called_once_with("./data/calculation_history.csv", "w")
    handle = mock_file()
    handle.truncate.assert_called_once()

    # Check that the DataFrame.to_csv was called to update the header
    mock_to_csv.assert_called_once_with("./data/calculation_history.csv", index=False)

    # Check that logging info was called correctly
    assert mock_logging_info.call_count == 2
    mock_logging_info.assert_any_call("History Deleted")
    mock_logging_info.assert_any_call("History Header updated")
