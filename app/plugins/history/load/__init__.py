"""Load Operation"""
import logging
import pandas as pd
from app.commands import Command

class LoadHistoryCommand(Command):
    """Load Operation using load"""
    def execute(self):
        try:
            # Assuming your history file is in CSV format
            history_file_path = "./data/calculation_history.csv"
            # Load the history file into a pandas DataFrame
            history_df = pd.read_csv(history_file_path)
            logging.info("Loading history...")
            print(history_df)
            logging.info("History Loaded")
        except:
            logging.error("Parsing data error")
