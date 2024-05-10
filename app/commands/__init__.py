'''Command pattern is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.'''
from abc import ABC, abstractmethod
import logging

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}
        logging.info("CommandHandler initialized.")

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command
        logging.info(f"Command '{command_name}' registered.")

    def execute_command(self, command_name: str):
        """ Look before you leap (LBYL) - Use when its less likely to work
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"No such command: {command_name}")
        """
        """Easier to ask for forgiveness than permission (EAFP) - Use when its going to most likely work"""
        try:
            logging.info(f"Executing command: {command_name}")
            self.commands[command_name].execute()
        except KeyError:
            logging.warning(f"No such command: {command_name}")
            print(f"No such command: {command_name}")

    def list_commands(self):
        # Return a list of all registered command names
        return list(self.commands.keys())
