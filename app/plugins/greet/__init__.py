'''Greetings Plugin'''
import logging
from app.commands import Command


class GreetCommand(Command):
    def execute(self):
        logging.info("Hello, World!")
        print("Hello, World!")
#This is just a template for the plugin. To make sure everything works before adding the calculator functions
