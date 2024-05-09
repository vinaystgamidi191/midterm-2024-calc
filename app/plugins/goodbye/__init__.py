'''Goodbye plugin'''
import logging
from app.commands import Command

class GoodbyeCommand(Command):
    def execute(self):
        # Log the goodbye message instead of printing it
        logging.info("Goodbye")
#This is just a template for the plugin. To make sure everything works before adding the calculator functions

