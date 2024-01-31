# Python - Almost a circle

This is a Python project that contains classes and methods to create and manipulate geometric shapes, such as rectangles and squares. The project also includes unit tests and a JSON serialization and deserialization mechanism.

## Requirements

- Python 3.8.5 or higher
- Pycodestyle 2.8 or higher
- Unittest module

## Usage

To use the classes and methods in this project, you need to import them from the models package:

```python
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
```

Then, you can create instances of the classes and use their attributes and methods. For example, to create a rectangle with width 10, height 2, x 1, y 9 and id 12:

```python
r1 = Rectangle(10, 2, 1, 9, 12)
```

To print the area of the rectangle:

```python
print(r1.area())
```

To update the attributes of the rectangle:

```python
r1.update(height=4)
```

To print the JSON representation of the rectangle:

```python
print(r1.to_dictionary())
```

## Testing

To test the classes and methods in this project, you need to run the tests using the unittest module. You can use the following command to run all the tests:

```bash
python3 -m unittest discover tests
```

You can also run a specific test file by using this command:

```bash
python3 -m unittest tests/test_models/test_base.py
```

The tests will check the functionality and the style of the code..
