## Python - Input/Output
This project contains Python scripts and test cases that demonstrate how to work with input and output operations in Python. The scripts cover topics such as reading and writing files, JSON serialization and deserialization, and documentation.

## Requirements
```python
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
Python Test Cases
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
All your test files should be text files (extension: .txt)
All your tests should be executed by using this command: python3 -m doctest ./tests/*
All your modules should have a documentation (python3 -c ‘print(import(“my_module”).doc)’)
All your classes should have a documentation (python3 -c ‘print(import(“my_module”).MyClass.doc)’)
All your functions (inside and outside a class) should have a documentation (python3 -c ‘print(import(“my_module”).my_function.doc)’ and python3 -c ‘print(import(“my_module”).MyClass.my_function.doc)’)
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
```
The following files are included in this project:

# 0-read_file.py: A function that reads a text file (UTF8) and prints it to stdout.
# 1-number_of_lines.py: A function that returns the number of lines of a text file.
# 2-read_lines.py: A function that reads n lines of a text file (UTF8) and prints it to stdout.
# 3-write_file.py: A function that writes a string to a text file (UTF8) and returns the number of characters written.
# 4-append_write.py: A function that appends a string at the end of a text file (UTF8) and returns the number of characters added.
# 5-to_json_string.py: A function that returns the JSON representation of an object (string).
# 6-from_json_string.py: A function that returns an object (Python data structure) represented by a JSON string.
# 7-save_to_json_file.py: A function that writes an Object to a text file, using a JSON representation.
# 8-load_from_json_file.py: A function that creates an Object from a “JSON file”.
# 9-add_item.py: A script that adds all arguments to a Python list, and then save them to a file.
# 10-class_to_json.py: A function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.
# 11-student.py: A class Student that defines a student by: first name, last name and age.
# 12-student.py: A class Student that defines a student by: first name, last name and age, with a method to retrieve a JSON representation of the instance.
# 13-student.py: A class Student that defines a student by: first name, last name and age, with methods to retrieve a JSON representation of the instance and to replace all attributes of the instance.
# 14-pascal_triangle.py: A function that returns a list of lists of integers representing the Pascal’s triangle of n.
# tests: A folder containing the test files for each script.
## Usage
To run the scripts, you need to have Python 3 installed on your system. You can execute the scripts as follows:
```bash
./<script_name>.py
```
To run the test cases, you need to have Python 3 and the doctest module installed on your system. You can execute the test cases as follows:
```bash
python3 -m doctest ./tests/<test_file>.txt
```
## Author
This project was created by [Israelshecktar](https://github.com/Israelshecktar)
