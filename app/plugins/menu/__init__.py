'''Menu command plugin for the command line interface.'''
import logging
from app.commands import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self):
        # Log the action of displaying the menu
        logging.info("Displaying available commands to the user.")
        
        print("Available commands:")
        for command_name in self.command_handler.list_commands():
            # Keeping print statements for direct user interaction
            print("-", command_name)
