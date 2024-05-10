''' This module contains tests for the CalculationHistory class. '''
import os
from unittest.mock import patch
import pytest
from app.calculation_history import CalculationHistory

# Fixture to reset singleton for each test
@pytest.fixture(autouse=True)
def reset_singleton():
    '''Reset the CalculationHistory singleton for each test.'''
    # Use a public reset method if available, or adjust your class design.
    CalculationHistory.reset_instance_for_testing()
    yield

# Ensure the CalculationHistory class can be instantiated
def test_calculation_history_singleton():
    '''Test that the CalculationHistory class is a singleton.'''
    history1 = CalculationHistory.instance()
    history2 = CalculationHistory.instance()
    assert history1 is history2

# Test loading or initializing the history
def test_load_or_initialize_history(tmp_path):
    '''Test loading or initializing the history.'''
    test_file = tmp_path / "test_history.csv"
    test_file.write_text("Expression,num1,num2,Result\nAddition,1,1,2")
    with patch.dict(os.environ, {"HISTORY_FILE_PATH": str(test_file)}):
        history = CalculationHistory.instance()
        assert not history.history_df.empty

# Test adding records and trimming to the last 10 records
def test_add_record():
    '''Test adding records to the history.'''
    history = CalculationHistory.instance()
    for i in range(15):  # Add 15 records
        history.add_record('Addition', i, i, i + i)
    assert len(history.history_df) == 10  # Only 10 records should remain

# Test saving the history to a file
def test_save_history(tmp_path):
    '''Test saving the history to a file.'''
    test_file = tmp_path / "test_history.csv"
    with patch.dict(os.environ, {"HISTORY_FILE_PATH": str(test_file)}), patch('os.makedirs'):
        history = CalculationHistory.instance()
        history.add_record('Addition', 1, 1, 2)
        history.save_history()
        assert test_file.exists()

# Test clearing the history
def test_clear_history():
    '''Test clearing the history.'''
    history = CalculationHistory.instance()
    history.add_record('Addition', 1, 1, 2)
    history.clear_history()
    assert history.history_df.empty

# Test deleting a record from the history
def test_delete_history():
    '''Test deleting a record from the history.'''
    history = CalculationHistory.instance()
    history.add_record('Addition', 1, 1, 2)
    initial_length = len(history.history_df)
    history.delete_history(0)
    assert len(history.history_df) == initial_length - 1

# Test loading the history from a file
def test_load_history(tmp_path):
    '''Test loading the history from a file.'''
    test_file = tmp_path / "test_history.csv"
    test_file.write_text("Expression,num1,num2,Result\nAddition,1,1,2")
    with patch.dict(os.environ, {"HISTORY_FILE_PATH": str(test_file)}):
        history = CalculationHistory.instance()
        assert history.load_history()

# Test loading the history from an empty file
def test_load_history_failure(tmp_path):
    '''Test loading the history from an empty file.'''
    test_file = tmp_path / "test_history.csv"
    test_file.write_text("")  # Empty file to trigger EmptyDataError
    with patch.dict(os.environ, {"HISTORY_FILE_PATH": str(test_file)}):
        history = CalculationHistory.instance()
        assert not history.load_history()
