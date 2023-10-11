# AirBnB Clone Command Interpreter

Welcome to the AirBnB clone project! This is the first step towards building a full web application that mimics the functionality of Airbnb. In this initial phase, we will develop a command-line interpreter that allows you to manage AirBnB objects. This command interpreter is a crucial component as it will be used in all subsequent phases of the project.

## Background Context

Before diving into the command interpreter, it's essential to familiarize yourself with the AirBnB concept, as this project aims to replicate its functionality. You should also read about the following topics:

- [cmd module](https://docs.python.org/3/library/cmd.html)
- [UUID module](https://docs.python.org/3/library/uuid.html)
- [datetime module](https://docs.python.org/3/library/datetime.html)
- [unittest module](https://docs.python.org/3/library/unittest.html)

The learning objectives of this project include creating a Python package, implementing a command interpreter using the cmd module, unit testing in a large project, serialization and deserialization of classes, working with JSON files, managing datetime, understanding UUIDs, and using *args and **kwargs.

## Command Interpreter

### What's a Command Interpreter?

Think of the command interpreter as a user interface for managing AirBnB objects. It's similar to a shell but tailored to the specific needs of this project. The command interpreter allows you to perform various operations on AirBnB objects, such as:

1. Create a new object (e.g., a new User or a new Place).
2. Retrieve an object from a file, database, or other sources.
3. Perform operations on objects (count, compute stats, etc.).
4. Update attributes of an object.
5. Destroy an object.

## How to Start the Command Interpreter

To start the command interpreter, follow these steps:

1. Ensure you are in the project directory.
2. Run the following command in your terminal:

```
./console.py
```

This will launch the command interpreter, and you will see a prompt where you can enter commands.

## How to Use the Command Interpreter

The command interpreter provides a set of commands to interact with AirBnB objects. Here are some essential commands and their usage:

- `create`: Create a new AirBnB object. Usage: `create <class name>`.
- `show`: Show the details of a specific AirBnB object. Usage: `show <class name> <object ID>`.
- `destroy`: Delete an AirBnB object. Usage: `destroy <class name> <object ID>`.
- `all`: List all AirBnB objects or objects of a specific class. Usage: `all` or `all <class name>`.
- `update`: Update attributes of an AirBnB object. Usage: `update <class name> <object ID> <attribute name> "<attribute value>"`.

For a complete list of available commands and their usage, type `help` within the command interpreter.

## Examples

Here are some examples of how to use the command interpreter:

1. Create a new User object:
   ```
   (hbnb) create User
   ```

2. Show details of a User object with ID `123`:
   ```
   (hbnb) show User 123
   ```

3. List all User objects:
   ```
   (hbnb) all User
   ```

4. Update the email of a User object with ID `456`:
   ```
   (hbnb) update User 456 email "newemail@example.com"
   ```

5. Delete a Place object with ID `789`:
   ```
   (hbnb) destroy Place 789
   ```

These are just basic examples. The command interpreter offers more functionality for managing AirBnB objects.

