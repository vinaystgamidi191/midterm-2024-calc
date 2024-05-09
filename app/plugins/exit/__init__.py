'''exit command plugin for the application'''
import sys
import logging
from app.commands import Command

class ExitCommand(Command):
    def execute(self):
        # Log the intention to exit the application
        logging.info("Exiting the application upon user request.")
        # Exit the application
        sys.exit("Exiting...")
