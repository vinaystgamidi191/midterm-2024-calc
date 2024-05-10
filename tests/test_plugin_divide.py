'''Test the 'divide' command in the app'''
import pytest
from app import App

def test_app_divide_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'divide' command, takes two numbers as input, and outputs their quotient."""
    # Setup the input for the 'divide' command followed by two numbers and then 'exit'
    inputs = iter(['divide', '10', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    # Check that the exit was graceful with the correct exit code
    assert e.value.code == 0, "The app did not exit as expected"

    # Capture the output from the 'divide' command
    out, _ = capfd.readouterr()

    # Assert that the quotient of the numbers was printed to stdout
    # Ensure the expected output matches exactly what your 'divide' command outputs, including any newlines or formatting
    expected_output = "The result of dividing 10.0 by 2.0 is: 5.0"
    assert expected_output in out, f"The 'divide' command did not produce the expected output. Got: {out}"

def test_app_divide_by_zero(capfd, monkeypatch):
    """Test that the REPL correctly handles division by zero."""
    inputs = iter(['divide', '10', '0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as _:
        app.start()

    out, _ = capfd.readouterr()
    expected_output = "Error: Cannot divide by zero"
    assert expected_output in out, f"Division by zero did not produce the expected error message. Got: {out}"

def test_app_divide_non_numeric(capfd, monkeypatch):
    """Test that the REPL handles non-numeric inputs properly."""
    inputs = iter(['divide', 'ten', 'five', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as _:
        app.start()

    out, _ = capfd.readouterr()
    expected_output = "Please enter valid numbers."
    assert expected_output in out, f"Non-numeric input did not produce the expected error message. Got: {out}"

@pytest.mark.parametrize("dividend, divisor, result", [
    ('-10', '2', '-5.0'),  # Negative divided by positive
    ('10', '-2', '-5.0'),  # Positive divided by negative
    ('-10', '-2', '5.0'),  # Negative divided by negative
])
def test_app_divide_negative_positive(capfd, monkeypatch, dividend, divisor, result):
    """Test division with various combinations of positive and negative numbers."""
    inputs = iter(['divide', dividend, divisor, 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    out, _ = capfd.readouterr()
    # Adjust the format here to match the actual output format
    expected_output = f"The result of dividing {float(dividend)} by {float(divisor)} is: {result}\n"
    assert expected_output in out, f"Division with {dividend}/{divisor} did not produce the expected output. Got: {out}"
