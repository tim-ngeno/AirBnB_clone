# 0x00. AirBnB clone - The console

## Overview
This repository entails the following aspects used to build a clone of the AirBnb website:

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file How to manage datetime
- What is an UUID
- What is `*args` and how to use it 
- What is `**kwargs` and how to use it
- How to handle named arguments in a function


## Description

The HBnB Command Line Interface (CLI) is a command interpreter developed as part of the HBnB project. The CLI allows users to interact with the HBnB system and manage various data objects, such as users, states, cities, amenities, places, and reviews.

## Usage

The HBnB CLI provides a set of commands to interact with the system. Here are some of the available commands and their descriptions:

- `quit`: Exit the command interpreter.
- `EOF`: End of file (Ctrl+D) to exit the interpreter.
- `create <class>`: Create a new instance of the specified class.
- `show <class> <id>`: Display the string representation of an instance.
- `destroy <class> <id>`: Delete an instance based on class name and id.
- `all [<class>]`: Display all instances or instances of a specific class.
- `help <command>`: Display help information for a specific command.

## Examples

1. Creating a new instance:
   ```bash
   (hbnb) create User
   ```

2. Showing an instance:
   ```bash
   (hbnb) show User 12345-6789
   ```

3. Destroying an instance:
   ```bash
   (hbnb) destroy State 98765-4321
   ```

4. Displaying all instances of a specific class:
   ```bash
   (hbnb) all Amenity
   ```
