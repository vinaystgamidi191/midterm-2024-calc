'''test_plugin_menu.py'''
from unittest.mock import Mock
from app.plugins.menu import MenuCommand

def test_menu_command_execute(capfd):
    """Test that the MenuCommand prints the available commands."""
    # Mock the command_handler and its list_commands method
    mock_command_handler = Mock()
    mock_command_handler.list_commands.return_value = ['command1', 'command2']

    # Create a MenuCommand instance with the mocked command_handler
    menu_command = MenuCommand(mock_command_handler)

    # Execute the command
    menu_command.execute()

    # Capture the output
    out, _ = capfd.readouterr()

    # Verify the output
    expected_output = "Available commands:\n- command1\n- command2\n"
    assert out == expected_output
    # Verify logging.info was called with expected message
    # This might require configuring the logging during the test or using a logging mocking library
