'''Multiplication plugin for calculator application'''
import logging
import pandas as pd
from app.commands import Command
from app.calculation_history import CalculationHistory
import os

class MultiplyCommand(Command):
    def execute(self):
        logging.info("Executing MultiplyCommand")
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 * num2
            print(f"The result of multiplying {num1} by {num2} is: {result}")
            logging.info(f"MultiplyCommand execution successful: {num1} * {num2} = {result}")

             # Get the singleton instance of CalculationHistory
            history = CalculationHistory.instance()
            # Use the add_record method to log the operation with correct column values
            history.add_record('Multiplication', num1, num2, result)

            # Define the CSV file path
            history_file_path = "./data/calculation_history.csv"
            # Check if the file exists and is not empty to determine if we should write headers
            file_exists = os.path.exists(history_file_path)
            write_header = not file_exists or os.stat(history_file_path).st_size == 0

            # Create a DataFrame to log this operation
            df = pd.DataFrame([[num1, num2, result]], columns=['Operand 1', 'Operand 2', 'Result'])
            # Append the operation to a CSV file, adding headers only if the file is new or empty
            df.to_csv(history_file_path, mode="a", header=write_header, index=False)
            logging.info(f"Multiplication history updated with result: {result}")

        except ValueError:
            print("Please enter valid numbers.")
            logging.error("Error in MultiplyCommand: Invalid input for numbers.")
