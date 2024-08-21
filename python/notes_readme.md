# Python Fundamental

Level: Important
Status: Next_to_Learn

## Learning Agenda:

1. Get started
    1. How a programming language works
    2. some root level of concept
2. Hello world
3. Variables
4. data tapes
    1. number
    2. string
    3. array
    4. object
    5. boolean
    6. Primitive and reference data 
5. Operators
6. Conditionals Statement
7. Control flow
8. Functions

### Additional

Software Engineering-related terms and words

---

### Understand the workflow of writing code in any programming language

1. chose a language - `Python`
2. write some code `print("hello world")`
3. run code using its compiler/interpreter/assembler
4. You got the output `hello world`

### But How is it done?

![download.png](Python%20Fundamental%2093431c0c8eac40a0a212672372f6b84c/download.png)

**Source code (main.py) > Python Interpreter > Running code**

***Try more briefly***

![download.png](Python%20Fundamental%2093431c0c8eac40a0a212672372f6b84c/download%201.png)

**Source Code:**

Source code is the fundamental component of a computer program that is created by a programmer, often written in the form of functions, descriptions, definitions, calls, methods, and other operational statements. It is designed to be human-readable and formatted in a way that developers and other users can understand.

**Interpreter:** 

An interpreter is a program that directly executes instructions written in a programming or scripting language, without requiring them to be compiled into a machine language program first. Here are some key points about interpreters:

- Interpreters translate and execute code line-by-line or statement-by-statement.
- They allow for more immediate execution and testing of code compared to compiled languages.
- Interpreted languages often provide more flexibility and ease of debugging, but may have slower execution times for complex programs compared to compiled languages.
- Examples of interpreted languages include Python, JavaScript, and Ruby.

**Compiler:**

Ah, the trusty compiler—a behind-the-scenes wizard that turns our human-readable code into something that machines can actually chew on! 🧙‍♂️ Let’s dive into this magical process, shall we?

**A compiler** is like the ultimate multilingual translator for computers. Imagine you’re at a global conference where everyone speaks a different language. You’ve got your eloquent speech prepared in English (your high-level programming language), but the audience consists of CPUs (Central Processing Units) who only understand their native tongue—machine language (or assembly language). What do you do? You call in the compiler!

![diagram.png](Python%20Fundamental%2093431c0c8eac40a0a212672372f6b84c/diagram.png)

- **Lexical Analysis**: It breaks down your code into smaller chunks (tokens) and figures out what each word means. Think of it as the grammar-checker for code.
- **Parsing**: It builds a syntax tree—a fancy family tree that shows how your code elements relate to each other. This tree helps the compiler understand the structure of your program.
- **Semantic Analysis**: The compiler checks if your code makes sense. Are you trying to add a banana to a giraffe? It’ll catch those quirks.
- **Intermediate Representation**: The compiler creates an intermediate form of your code. It’s like a secret code that’s easier for the compiler to manipulate.
- **Optimization**: The compiler puts on its Sherlock Holmes hat and looks for ways to make your code faster, smaller, and more efficient. It’s all about performance!
- **Code Generation**: Finally, it translates your optimized, intermediate code into low-level machine instructions. These are the binary commands that the CPU can execute directly.

**Byte Code:**

![Capture-660x190.png](Python%20Fundamental%2093431c0c8eac40a0a212672372f6b84c/Capture-660x190.png)

Bytecode is **a low-level representation of the instructions in a programming language**. In the case of Python, the CPython interpreter uses a particular kind of bytecode known as CPython bytecode. It functions as a collection of guidelines that specify the activities the interpreter should do.

**Virtual Machine:**

![Architecture of python virtual mechines](Python%20Fundamental%2093431c0c8eac40a0a212672372f6b84c/frame.png)

Architecture of python virtual mechines

Certainly! Let’s break down the Python Virtual Machine (PVM) in a way that won’t make your brain feel like it’s doing gymnastics. 🤸‍♂️

1. **The Setup**: Imagine you’re hosting a fancy dinner party (Python program). You’ve got your recipe (Python code) ready, but you need someone to cook it. That’s where the PVM comes in!
2. **The Interpreter**: Think of the Python interpreter as your personal chef. It reads your recipe (Python code) line by line. But instead of chopping veggies and sautéing onions, it translates each line into a secret code (bytecode). This bytecode is like a cryptic set of instructions that the PVM can understand.
3. **Enter the PVM**: The PVM is like the kitchen where the magic happens. It’s a cozy little room where the interpreter brings its secret codes. Here’s what happens inside:
    - **Bytecode Conversion**: The PVM takes the bytecode and converts it into something the computer can actually chew on. It’s like turning your recipe into a step-by-step manual for the kitchen appliances.
    - **Stack Time**: The PVM is stack-based, which means it uses a stack (like a Jenga tower) to keep track of things. When you add two numbers, they go on the stack. When you multiply, it’s another layer. The PVM keeps stacking and unstacking as it follows your recipe.
4. **Cooking Up Results**: As the PVM follows the instructions, it performs operations—adding, subtracting, comparing, and more. The results of these operations live on the stack. It’s like the PVM has a little whiteboard where it scribbles down intermediate answers.
5. **Ta-Da! Executable Code**: Finally, the PVM serves up the fully cooked dish—the executable code. It’s like presenting your beautifully plated meal to hungry guests (or in this case, the computer). The computer happily munches on those instructions and does what you asked it to do.

---

## **Some Basic Concepts of Programming**

Understanding root-level concepts is essential when learning to program, as they form the foundation upon which more advanced topics are built. Here are some core concepts:

### 1. **Variables and Data Types**

![download.png](Python%20Fundamental%2093431c0c8eac40a0a212672372f6b84c/download%202.png)

- **Variables:** Containers for storing data values. They allow you to reference and manipulate data.
    - Example: `x = 10`
- **Data Types:** The type of data that a variable can hold (e.g., integers, floats, strings, booleans).
    - Example: `int` (integer), `float` (decimal number), `str` (string of characters), `bool` (true/false).
    
    ![python-data-types.png](Python%20Fundamental%2093431c0c8eac40a0a212672372f6b84c/python-data-types.png)
    
    **Code Example:**
    

```python
#intiger
age = 30
num_apples = 20

#Floating-point
pi = 3.1416

#string
name = "Alice"
message = 'Hello, World!'

#List
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]

#tuples
rgb_color = ("red", "green", "blue")
coordinates = (10, 30)

#dictionary
person = {"name": "Bob", "age": 25, "city": "New York"}
grades = {"math": 90, "history": 85, "science": 92}

#sets
vowels = {'a', 'e', 'i', 'o', 'u'}
prime_numbers = set([2, 3, 5, 7, 11])

#Boolean
is_sunny = True
has_subscription = False

#None Type
result = None
```

### 2. **Control Structures**

- **Conditional Statements:** `if`, `else`, and `elif` (or `switch` in some languages) allow your code to make decisions.
    
    ![control-flow-in-java2.png](Python%20Fundamental%2093431c0c8eac40a0a212672372f6b84c/control-flow-in-java2.png)
    
    - Example:
        
        ```python
        pythonCopy code
        if temperature > 30:
            print("It's hot!")
        else:
            print("It's cool!")
        
        ```
        
- **Loops:** Repeat a block of code multiple times. The most common loops are `for` and `while`.
    - Example (Python):
        
        ```python
        pythonCopy code
        for i in range(5):
            print(i)
        
        ```
        

### 3. **Functions**

- A function is a block of reusable code that performs a specific task.
- Functions can take inputs (parameters) and may return an output.
    
    ![download.png](Python%20Fundamental%2093431c0c8eac40a0a212672372f6b84c/download%203.png)
    
    - Example:
        
        ```python
        pythonCopy code
        def add(a, b):
            return a + b
        result = add(2, 3)  # result is 5
        
        ```
        

### 4. **Data Structures**

- **Arrays/Lists:** Ordered collections of items that can be indexed.
    - Example (Python list): `fruits = ["apple", "banana", "cherry"]`
- **Dictionaries/Maps:** Collections of key-value pairs.
    - Example (Python dictionary): `person = {"name": "John", "age": 30}`
- **Stacks and Queues:** Special types of data structures used to manage data in a particular order.

### 5. **Algorithms**

- **Sorting:** Techniques to arrange data in a specific order (e.g., bubble sort, quicksort).
- **Searching:** Methods to find data within a structure (e.g., linear search, binary search).

### 6. **Object-Oriented Programming (OOP)**

- **Classes and Objects:** Classes are blueprints for creating objects (instances). They encapsulate data and behavior.
    
    ![illustration.svg](Python%20Fundamental%2093431c0c8eac40a0a212672372f6b84c/illustration.svg)
    
    - Example:
        
        ```python
        pythonCopy code
        class Dog:
            def __init__(self, name):
                self.name = name
        
            def bark(self):
                print(f"{self.name} says woof!")
        
        ```
        
- **Inheritance:** A mechanism where one class can inherit attributes and methods from another.
- **Encapsulation:** Hiding internal states and requiring all interaction to be performed through methods.
- **Polymorphism:** The ability to process objects differently based on their data type or class.

### 7. **Recursion**

- A function that calls itself to solve smaller instances of a problem until it reaches a base case.
    
    ![images.png](Python%20Fundamental%2093431c0c8eac40a0a212672372f6b84c/images.png)
    
    - Example:
        
        ```python
        pythonCopy code
        def factorial(n):
            if n == 1:
                return 1
            else:
                return n * factorial(n-1)
        
        ```
        

### 8. **Memory Management**

- **Stack and Heap:** The two areas of memory where data is stored. Stack for static memory allocation, heap for dynamic memory allocation.
- **Garbage Collection:** Automatic memory management to reclaim memory occupied by objects that are no longer in use.

### 9. **Error Handling**

- Mechanisms to handle runtime errors gracefully (e.g., `try`, `except` in Python).
    - Example:
        
        ```python
        pythonCopy code
        try:
            result = 10 / 0
        except ZeroDivisionError:
            print("You can't divide by zero!")
        
        ```
        

### 10. **Input/Output Operations**

- **File Handling:** Reading from and writing to files.
    - Example:
        
        ```python
        pythonCopy code
        with open('file.txt', 'r') as file:
            content = file.read()
        
        ```
        

These root-level concepts are fundamental in almost every programming language and form the basis for more complex topics. Mastering them will set you up for success in any programming endeavor.