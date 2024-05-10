'''App module'''
import os
import pkgutil
import importlib
import sys
from app.command import CommandHandler, Command
from dotenv import load_dotenv
import logging
import logging.config


class App:
   def __init__(self):
       os.makedirs('logs', exist_ok=True)
       self.configure_logging()
       load_dotenv()
       self.settings = self.load_environment_variables()
       self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
       self.command_handler = CommandHandler()


   def configure_logging(self):
       logging_conf_path = 'logging.conf'
       if os.path.exists(logging_conf_path):
           logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
       else:
           logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
       logging.info("Logging configured.")



   def load_environment_variables(self):
       settings = {key: value for key, value in os.environ.items()}
       logging.info("Environment variables  loaded.")
       return settings


   def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
       return self.settings.get(env_var, None)


   def load_plugins(self):
       plugins_package = 'app.plugins'
       plugins_path = plugins_package.replace('.', '/')
       if not os.path.exists(plugins_path):
           logging.warning(f"Plugins directory '{plugins_path}' not found.")
           return
       for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
           if is_pkg:
               try:
                   plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                   self.register_plugin_commands(plugin_module, plugin_name)
               except ImportError as e:
                   logging.error(f"Error importing plugin {plugin_name}: {e}")


   def register_plugin_commands(self, plugin_module, plugin_name):
       for item_name in dir(plugin_module):
           item = getattr(plugin_module, item_name)
           if isinstance(item, type) and issubclass(item, Command) and item is not Command:
               # Handle special case for MenuCommand or others that require additional arguments
               if plugin_name == 'menu':  # Adjust this condition based on your plugin naming
                   command_instance = item(self.command_handler)
               else:
                   command_instance = item()
               self.command_handler.register_command(plugin_name, command_instance)
               logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

   def register_history_commands(self):
    history_plugin_base = 'app.plugins.history'
    history_commands = ['load', 'save', 'clear', 'delete']  # Add other subcommands as needed

    for command_name in history_commands:
        try:
            # Dynamically import the command module from the history subpackage
            command_module_path = f'{history_plugin_base}.{command_name}'
            command_module = importlib.import_module(command_module_path)

            # Iterate over items in the module and register command instances
            for item_name in dir(command_module):
                item = getattr(command_module, item_name)
                if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                    command_instance = item(self.command_handler) if hasattr(item, 'requires_command_handler') else item()
                    self.command_handler.register_command(f'history.{command_name}', command_instance)
                    logging.info(f"History command '{command_name}' registered.")
        except ImportError as e:
            logging.error(f"Error loading history command {command_name}: {e}")

   def start(self):
       self.load_plugins()
       self.register_history_commands()
       logging.info("Application started. Type 'exit' to exit.")
       try:
           while True:
               cmd_input = input(">>> ").strip()
               if cmd_input.lower() == 'exit':
                   logging.info("Application exit.")
                   sys.exit(0)
               try:
                   self.command_handler.execute_command(cmd_input)
               except KeyError:
                   logging.error(f"Unknown command: {cmd_input}")
                   sys.exit(1)
       except KeyboardInterrupt:
           logging.info("Application interrupted and exiting gracefully.")
           sys.exit(0)
       finally:
           logging.info("Application shutdown.")


if __name__ == "__main__":
   app = App()
   app.start()