'''This file contains the tests for the 'subtract' command in the app'''
import pytest
from app import App

def test_app_substract_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'subtract' command, takes two numbers as input, and outputs their difference."""
    # Setup the input for the 'subtract' command followed by two numbers and then 'exit'
    inputs = iter(['substract', '10', '3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    # Check that the exit was graceful with the correct exit code
    assert e.value.code == 0, "The app did not exit as expected"

    # Capture the output from the 'subtract' command
    out, _ = capfd.readouterr()

    # Assert that the difference of the numbers was printed to stdout
    # Ensure the expected output matches exactly what your 'subtract' command outputs, including any newlines or formatting
    expected_output = "The result of subtracting 3.0 from 10.0 is: 7.0"
    assert expected_output in out, f"The 'subtract' command did not produce the expected output. Got: {out}"

@pytest.mark.parametrize("minuend, subtrahend, expected_output", [
    ('10', '3', "The result of subtracting 3.0 from 10.0 is: 7.0\n"),  # Standard subtraction
    ('-5', '3', "The result of subtracting 3.0 from -5.0 is: -8.0\n"),  # Negative minuend
    ('5', '-3', "The result of subtracting -3.0 from 5.0 is: 8.0\n"),  # Negative subtrahend
    ('0', '5', "The result of subtracting 5.0 from 0.0 is: -5.0\n"),  # Zero minuend
    ('5', '0', "The result of subtracting 0.0 from 5.0 is: 5.0\n"),  # Zero subtrahend
    ('123456789', '987654321', "The result of subtracting 987654321.0 from 123456789.0 is: -864197532.0\n"),  # Large numbers
])
def test_app_substract_variations(capfd, monkeypatch, minuend, subtrahend, expected_output):
    """Test the 'subtract' command with various inputs."""
    inputs = iter(['substract', minuend, subtrahend, 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    out, _ = capfd.readouterr()
    assert expected_output in out, f"Subtract command with inputs {minuend} and {subtrahend} did not produce the expected output. Got: {out}"

def test_app_substract_non_numeric(capfd, monkeypatch):
    """Test the 'subtract' command with non-numeric input."""
    inputs = iter(['substract', 'ten', 'three', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    out, _ = capfd.readouterr()
    expected_error_message = "Please enter valid numbers."
    assert expected_error_message in out, "Non-numeric input did not produce the expected error message."
