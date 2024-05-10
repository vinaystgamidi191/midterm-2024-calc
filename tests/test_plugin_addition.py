'''This file contains the tests for the 'addition' command in the app'''
import pytest
from app import App

def test_app_addition_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'add' command, takes two numbers as input, and outputs their sum."""
    # Setup the input for the 'add' command followed by two numbers and then 'exit'
    inputs = iter(['addition', '3', '5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    # Check that the exit was graceful with the correct exit code
    assert e.value.code == 0, "The app did not exit as expected"

    # Capture the output from the 'add' command
    out, _ = capfd.readouterr()

    # Assert that the sum of the numbers was printed to stdout
    # Ensure the expected output matches exactly what your 'add' command outputs, including any newlines or formatting
    expected_output = "The sum is: 8.0"
    assert expected_output in out, f"The 'addition' command did not produce the expected output. Got: {out}"

@pytest.mark.parametrize("input1, input2, expected_output", [
    ('3', '5', "The sum is: 8.0\n"),  # Standard addition
    ('-3', '-5', "The sum is: -8.0\n"),  # Addition with negative numbers
    ('3', '-3', "The sum is: 0.0\n"),  # Sum resulting in zero
    ('123456789', '987654321', "The sum is: 1111111110.0\n"),  # Large numbers
    ('3.5', '2.5', "The sum is: 6.0\n"),  # Decimal numbers
])
def test_app_addition_variations(capfd, monkeypatch, input1, input2, expected_output):
    """Test the 'addition' command with various inputs."""
    inputs = iter(['addition', input1, input2, 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    out, _ = capfd.readouterr()
    assert expected_output in out, f"Addition command with inputs {input1} and {input2} did not produce the expected output. Got: {out}"

def test_app_addition_non_numeric(capfd, monkeypatch):
    """Test the 'addition' command with non-numeric input."""
    inputs = iter(['addition', 'notANumber', '5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    out, _ = capfd.readouterr()
    expected_error_message = "Please enter valid numbers."
    assert expected_error_message in out, "Non-numeric input did not produce the expected error message."
