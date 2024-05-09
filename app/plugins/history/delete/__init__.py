# app/plugins/history/delete/__init__.py
import logging
import pandas as pd
from app.commands import Command

class DeleteHistoryCommand(Command):
    """Delete specific records from the calculation history"""
    def execute(self, indexes_to_delete=[]):  # Adjusted to accept indexes_to_delete
        history_file_path = "./data/calculation_history.csv"
        try:
            # Load the existing history
            history_df = pd.read_csv(history_file_path)

            # Delete specified records, handling if indexes are out of bounds
            history_df.drop(index=indexes_to_delete, inplace=True, errors='ignore')
            history_df.reset_index(drop=True, inplace=True)

            # Save the updated history
            history_df.to_csv(history_file_path, index=False)
            logging.info(f"Deleted records at indexes: {indexes_to_delete}")
        except Exception as e:
            logging.error(f"Failed to delete history records: {str(e)}")
