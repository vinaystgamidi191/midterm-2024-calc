'''Divide plugin for the calculator application'''
import logging
import pandas as pd
from app.commands import Command
from app.calculation_history import CalculationHistory
import os

class DivideCommand(Command):
    def execute(self):
        logging.info("Executing DivideCommand")
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                logging.error("Attempted division by zero.")
            else:
                result = num1 / num2
                print(f"The result of dividing {num1} by {num2} is: {result}")
                logging.info(f"DivideCommand execution successful: {num1} / {num2} = {result}")

                # Get the singleton instance of CalculationHistory
                history = CalculationHistory.instance()
                # Use the add_record method to log the operation with correct column values
                history.add_record('Divide', num1, num2, result)

                # Define the CSV file path
                history_file_path = "./data/calculation_history.csv"
                # Check if the file exists and is not empty to determine if we should write headers
                file_exists = os.path.exists(history_file_path)
                write_header = not file_exists or os.stat(history_file_path).st_size == 0

                # Create a DataFrame to log this operation
                df = pd.DataFrame([[num1, num2, result]], columns=['Operand 1', 'Operand 2', 'Result'])
                # Append the operation to a CSV file, adding headers only if the file is new or empty
                df.to_csv(history_file_path, mode="a", header=write_header, index=False)
                logging.info(f"Division history updated with result: {result}")

        except ValueError:
            print("Please enter valid numbers.")
            logging.error("Invalid input for numbers.")
