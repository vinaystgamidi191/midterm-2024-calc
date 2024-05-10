'''This file contains the tests for the 'multiplication' command in the app'''
import pytest
from app import App

def test_app_multiply_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'multiply' command, takes two numbers as input, and outputs their product."""
    # Setup the input for the 'multiply' command followed by two numbers and then 'exit'
    inputs = iter(['multiplication', '4', '5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    # Check that the exit was graceful with the correct exit code
    assert e.value.code == 0, "The app did not exit as expected"

    # Capture the output from the 'multiply' command
    out, _ = capfd.readouterr()

    # Assert that the product of the numbers was printed to stdout
    # Ensure the expected output matches exactly what your 'multiply' command outputs, including any newlines or formatting
    expected_output = "The result of multiplying 4.0 by 5.0 is: 20.0"
    assert expected_output in out, f"The 'multiply' command did not produce the expected output. Got: {out}"

    # Optionally, include additional checks or variations to test different input scenarios
@pytest.mark.parametrize("input1, input2, expected_output", [
    ('0', '5', "The result of multiplying 0.0 by 5.0 is: 0.0\n"),  # Multiplication with zero
    ('-3', '6', "The result of multiplying -3.0 by 6.0 is: -18.0\n"),  # Negative numbers
    ('123456789', '987654321', "The result of multiplying 123456789.0 by 987654321.0 is: 1.2193263111263526e+17\n"),  # Large numbers, updated expected output
    ('3.5', '2', "The result of multiplying 3.5 by 2.0 is: 7.0\n"),  # Decimal numbers
])
def test_app_multiply_variations(capfd, monkeypatch, input1, input2, expected_output):
    """Test the 'multiply' command with various inputs."""
    inputs = iter(['multiplication', input1, input2, 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as _:
        app.start()

    out, _ = capfd.readouterr()
    assert expected_output in out, f"Multiply command with inputs {input1} and {input2} did not produce the expected output. Got: {out}"

def test_app_multiply_non_numeric(capfd, monkeypatch):
    """Test the 'multiply' command with non-numeric input."""
    inputs = iter(['multiplication', 'notANumber', '5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as _:
        app.start()

    out, _ = capfd.readouterr()
    expected_output = "Please enter valid numbers."
    assert expected_output in out, "Non-numeric input did not produce the expected error message."
