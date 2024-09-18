
# Python Functions and Modules

## Python Functions
A **function** is a reusable block of code that performs a specific task. Functions help in organizing code, improving readability, and enabling code reuse.

### Defining a Function
You can define a function using the `def` keyword followed by the function name and parentheses `( )`.

```python
def greet(name):
    return f"Hello, {name}!"

# Call the function
print(greet("Mojahid"))
```

**Explanation:**
- `def greet(name)` defines a function named `greet` that takes a single argument `name`.
- `return` sends a value back when the function is called.
- `print(greet("Mojahid"))` calls the `greet` function, passing "Mojahid" as an argument.

### Function with Multiple Arguments
```python
def add_numbers(a, b):
    return a + b

# Call the function
result = add_numbers(10, 5)
print(result)
```

Here, `add_numbers` takes two arguments and returns their sum.

### Default Arguments
You can assign default values to parameters, which will be used if no argument is passed.

```python
def greet(name="User"):
    return f"Hello, {name}!"

print(greet())        # Uses default value
print(greet("Mojahid"))  # Overrides default value
```

---

## Python Modules
A **module** is a file that contains Python code, like functions, variables, and classes, that can be imported into other Python scripts. You can use built-in modules or create your own.

### Importing a Module
To use a module, you can import it with the `import` keyword.

```python
# Importing built-in math module
import math

# Using a function from the math module
print(math.sqrt(16))  # Prints 4.0
```

### Importing Specific Functions
You can import only specific functions from a module.

```python
from math import sqrt

print(sqrt(25))  # Prints 5.0
```

### Creating and Importing Your Own Module
1. Create a file called `my_module.py`:
```python
# my_module.py
def greet(name):
    return f"Welcome, {name}!"
```

2. Import and use the function in another script:
```python
# main.py
import my_module

print(my_module.greet("Mojahid"))
```

This allows you to organize your code into separate files.
