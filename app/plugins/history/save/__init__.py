''' Save History Command '''
import logging
from app.commands import Command
from app.calculation_history import CalculationHistory

class SaveHistoryCommand(Command):
    """Save Operation using save"""
    def execute(self):
        # Access the CalculationHistory instance
        history_manager = CalculationHistory()

        try:
            # Use the instance method to save the current history state
            history_manager.save_history()
            logging.info("Saving history...")
            logging.info(f"History saved successfully to {history_manager.history_file}")
        except Exception as e:
            logging.error(f"Failed to save history due to: {str(e)}")
