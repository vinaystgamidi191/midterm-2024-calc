# midterm-2024-calc
complex calculator
## Setup Instructions
1. Clone the repo
2. CD into the project folder
3. Create a virtual environment
4. Activate the virtual environment (VE)
5. Install Requirements
6. run 'main.py' 

## Test Commands
- `pytest` run all tests
- `pytest --pylint --cov` <- Run Pylint and Coverage (Can be run independently)

# Usage

## Functionlity

### Calculator Operations:

Basic arithmetic operations like add, subtract, multiply, and divide can be performed. With the help of the plugin architecture and dynamic loading design, we can add new features dynamically in the plugins folder without any hardcoding.

commands for the specific operation:

- `addition` - Addition
- `substract` - Subtraction
- `multiplication` - Multiplication
- `divide` - Division
- `menu` - Shows the list of commands
- `exit` - Exit the application
  
Dont worry about greet, exit and goodbye, those are just templates, feel free to modify them as you like.

menu command is to show all the available commands and will append the list if any new plugin is added in the future. The plugin names are parsed directly to show the list.

### History Management:

Effective data management methods are employed to handle the data.

commands to handle the data:

- `load` - Loads the history of operations performed
- `clear` - Clears the history
- `delete` - Deletes only specified index data 
- `save` - Saves your history of operations performed

./data/calculation_history.csv contains the history of operations. The system effectively reads and writes the CSV file.

### Configuration via Environment Variables:

The application configuration details, development, and testing environment variables are stored in .env file.

https://github.com/vinaystgamidi191/midterm-2024-calc/blob/280093897b454e2215b02bed8020191d51028163/app/__init__.py#L32C1-L40C1 


### REPL Interface:

This application works on the Read-Evaluate-Print-Loop pattern.



## Design Patterns

### Implementation and Application:

This application used and implemented various design patterns. *Facade pattern* was used for the Pandas data manipulation. The *Command pattern* is the REPL structure the application has and the application's code structure is flexible and scalable using *Factory Method*, *Singleton*, and *Strategy Patterns*.

The provided implementation demonstrates the use of several design patterns:

1. **Singleton Pattern**:
   The `App` class serves as a singleton by ensuring that only one instance of the class can exist within the application. This is achieved by having a private constructor and a static method (`__init__`) that controls the instantiation of the class.

https://github.com/vinaystgamidi191/midterm-2024-calc/blob/280093897b454e2215b02bed8020191d51028163/app/__init__.py#L11-L19


2. **Factory Method Pattern**:
   The `CommandHandler` class acts as a factory for creating command objects (`Command` instances). It provides a method `register_command` to register different types of commands and another method `execute_command` to execute these commands based on their names.

https://github.com/vinaystgamidi191/midterm-2024-calc/blob/280093897b454e2215b02bed8020191d51028163/app/__init__.py#L10-L32
 

3. **Command Pattern**:
   The `Command` abstract base class defines an interface for executing commands (`execute` method). Concrete command classes (for example `AddCommand`) implement this interface, encapsulating specific operations. This pattern decouples the sender (invoker of commands) from the receiver (objects performing the actions), allowing for extensibility and flexibility.

  https://github.com/vinaystgamidi191/midterm-2024-calc/blob/280093897b454e2215b02bed8020191d51028163/app/__init__.py#L8-L10

4. **Iterator Pattern**:
   The `load_plugins` method in the `App` class iterates over all modules in the `app.plugins` package using `pkgutil.iter_modules`. It dynamically loads and initializes plugin classes, demonstrating the use of the iterator pattern to traverse through a collection of items (modules) without exposing the underlying representation.

  https://github.com/vinaystgamidi191/midterm-2024-calc/blob/280093897b454e2215b02bed8020191d51028163/app/__init__.py#L40-L53

5. **Template Method Pattern**: The `Command` class defines an abstract method `execute()`, which concrete command classes must implement. This enforces a template for executing commands, allowing for customization of specific operations while maintaining a consistent interface across different commands.



6. **Strategy Pattern** (implied): While not explicitly implemented as a separate class, the `execute()` method in each concrete command class represents a strategy for performing specific operations. By encapsulating these strategies within command objects, the application can dynamically select and execute different strategies at runtime.

### Try/Catch/Except
Implemented exceptions to illustrate "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP)

 https://github.com/vinaystgamidi191/midterm-2024-calc/blob/280093897b454e2215b02bed8020191d51028163/app/__init__.py#L8-L37

  ## Testing and Code Quality

### Comprehensive tests using pytest:

The test cases are in the folder tests. Majorly used unit testing and assertions to check all possible outcomes. These test cases helped to increase the application's robustness.

- `pytest` run all tests
- `pytest --pylint --cov` <- Run Pylint and Coverage (Can be run independently)

test coverage = 96%

## Version Control, Documentation, and Logging

GitHub Actions performs all the tests while pushing or merging the code.

### Commit History:

This repo has kept a sequential and informative commit history for any reference

### Logging Practices:

Dynamic logging configuration through environment variables is performed. A professional logging system is designed and logs will contain all the critical steps while performing any operation. Detailed application operations, data manipulations, errors, and informational messages are provided using Logging. This system also retrieves and displays errors and handles exceptions without crashing the applications. Logging is majorly used in this application rather than print statements.

- `logging.info`- logs what happened in the line of code
- `logging.error` - logs the error that occurred after the line of code

https://github.com/vinaystgamidi191/midterm-2024-calc/blob/280093897b454e2215b02bed8020191d51028163/app/__init__.py#L8-L19