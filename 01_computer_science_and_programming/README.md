### 1. Introduction to Computer Science and Programming
# Table of Contents
1. [﻿Introduction to Computer Science and Programming](https://#introduction-to-computer-science-and-programming) 
1.1 [﻿Basic Computer Science Concepts](https://#basic-computer-science-concepts) 
    - [﻿What is a computer?](https://#what-is-a-computer) 
    - [﻿How does a computer work?](https://#how-does-a-computer-work) 
    - [﻿Binary and data representation](https://#binary-and-data-representation) 
    - [﻿Introduction to algorithms and computational thinking](https://#introduction-to-algorithms-and-computational-thinking) 
1.2 [﻿Fundamental Programming Concepts](https://#fundamental-programming-concepts) 
    - [﻿What is programming?](https://#what-is-programming) 
    - [﻿Programming paradigms (imperative, object-oriented, functional)](https://#programming-paradigms-imperative-object-oriented-functional) 
    - [﻿High-level vs. low-level languages](https://#high-level-vs-low-level-languages) 
    - [﻿Compilers and interpreters](https://#compilers-and-interpreters) 
    - [﻿Glossary of Programming](https://#glossary-of-programming) 
1.3 [﻿Introduction to Python](https://#introduction-to-python) 
    - [﻿History and philosophy of Python](https://#history-and-philosophy-of-python) 
    - [﻿Installing Python and setting up the development environment](https://#installing-python-and-setting-up-the-development-environment) 
    - [﻿Running your first Python program](https://#running-your-first-python-program) 

#### 1.1 Basic Computer Science Concepts
**What is a Computer?**

- A computer is an electronic device that processes data according to a set of instructions (programs) to perform various tasks. It can take input, process it, and produce output. A typical computer system consists of hardware (physical components like CPU, memory, etc.) and software (programs and operating systems).
**How Does a Computer Work?**

- A computer works through the interaction of its core components:
    - **Input Devices**: Accept data (e.g., keyboard, mouse).
    - **Central Processing Unit (CPU)**: The "brain" of the computer that processes instructions.
    - **Memory (RAM)**: Temporary storage that the CPU uses to store and retrieve data quickly.
    - **Storage Devices**: Long-term data storage (e.g., hard drives, SSDs).
    - **Output Devices**: Display processed data (e.g., monitor, printer).
The basic steps are:

1. **Input**: Data is received through input devices.
2. **Processing**: The CPU processes the data using instructions from software.
3. **Storage**: Data may be stored for later use.
4. **Output**: Processed data is sent to output devices.
**Binary and Data Representation**

- **Binary**: Computers operate using binary (base-2) number systems, which consist of two digits: 0 and 1. Every piece of data, whether text, images, or instructions, is represented in binary code.
- **Data Representation**: Data in computers is represented in binary form. For example:
    - **Numbers**: Represented directly in binary (e.g., the decimal number 5 is `101`  in binary).
    - **Text**: Represented using character encoding like ASCII, where each character has a specific binary value (e.g., 'A' is `01000001`  in binary).
**Introduction to Algorithms and Computational Thinking**

- **Algorithm**: A step-by-step procedure or a set of rules for solving a specific problem. In programming, algorithms are written in a language that the computer can understand.
- **Computational Thinking**: A problem-solving process that involves breaking down complex problems into smaller, more manageable parts (decomposition), recognizing patterns, abstracting general principles, and designing algorithms.
Example of an algorithm (to find the largest number in a list):

1. Start with the first number as the largest.
2. Compare the current largest number with the next number in the list.
3. If the next number is larger, update the largest number.
4. Repeat until the end of the list.
5. The largest number at the end is the result.
### 1.2 Fundamental Programming Concepts
**What is Programming?**

- **Programming** is the process of creating instructions that a computer can follow to perform specific tasks. These instructions are written in a programming language and define how data should be manipulated and how tasks should be executed. Programming allows us to control the behavior of computers and develop software applications.
**Programming Paradigms**

- **Imperative Programming**:
    - Focuses on describing **how** to perform tasks using a sequence of statements that change the program's state.
    - Examples: C, Python, Java.
    - **Example in Python**: Imperative approach to find the sum of numbers in a list
```python
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print(total)
```
- **Object-Oriented Programming (OOP)**:
    - Focuses on **objects** and **classes** to represent real-world entities. Emphasizes encapsulation, inheritance, and polymorphism.
    - Examples: Java, C++, Python.
```python
**## Example in Python**:
  

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}."

person = Person("Alice", 30)
print(person.greet())
```
- **Functional Programming**:
    - Focuses on **functions** and their application. Emphasizes immutability and avoids changing state.
    - Examples: Haskell, Lisp, Python (to some extent).
```
**## Example in Python**: Functional approach to find the sum of numbers in a list
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)
```
**High-level vs. Low-level Languages**

- **High-level Languages**:
    - Closer to human languages and easier to read and write. They abstract away most of the hardware details.
    - Examples: Python, Java, JavaScript.
    - **Features**: Easier syntax, built-in libraries, automatic memory management.
- **Low-level Languages**:
    - Closer to machine code and provide little abstraction from the computer's hardware.
    - Examples: Assembly, C.
    - **Features**: More control over hardware, efficient execution, but more complex syntax.
**Compilers and Interpreters**

- **Compiler**:
    - Translates the entire source code into machine code (binary) before execution.
    - Example: GCC for C/C++.
    - **Advantages**: Fast execution time, optimized code.
    - **Disadvantages**: Compilation can be time-consuming.
- **Interpreter**:
    - Translates and executes the source code line by line at runtime.
    - Example: Python Interpreter.
    - **Advantages**: Easier debugging, immediate feedback.
    - **Disadvantages**: Slower execution time.
**Glossary of Programming**

- **Algorithm**: A step-by-step procedure for solving a problem.
- **Variable**: A storage location identified by a name that holds a value.
- **Function**: A block of code designed to perform a specific task.
- **Class**: A blueprint for creating objects (OOP).
- **Object**: An instance of a class (OOP).
- **Inheritance**: Mechanism where a new class derives properties and behavior from an existing class (OOP).
- **Polymorphism**: Ability to process objects differently based on their data type or class (OOP).
- **Encapsulation**: Hiding the internal state and requiring all interactions to be performed through an object's methods (OOP).
- **Syntax**: The set of rules that defines the structure of valid statements in a programming language.
- **Debugging**: The process of finding and fixing errors in the code.


### 1.3 Introduction to Python
**History and Philosophy of Python**

- **History**:
    - Python was created by **Guido van Rossum** and first released in **1991**.
    - Python 2.x was widely used, but support for it has ended as of **January 1, 2020**.
    - Python 3.x is the current and actively developed version. It introduced many improvements and features over Python 2.x.
- **Philosophy**:
    - Python's philosophy emphasizes code readability and simplicity. This is reflected in the **Zen of Python**, a collection of guiding principles for writing computer programs in Python, which can be accessed by running `import this`  in a Python interpreter.
    - Key principles include:
        - **Readability counts**: Code should be easy to read and understand.
        - **There should be one—and preferably only one—obvious way to do it**: Python prefers one clear way to perform tasks.
        - **Simple is better than complex**: Aim for simplicity in code.
**Installing Python and Setting Up the Development Environment**

1. **Download Python**:
    - Visit the [﻿official Python website](https://www.python.org/downloads/) .
    - Download the installer for your operating system (Windows, macOS, Linux).
2. **Install Python**:
    - **Windows**: Run the installer and ensure you check the box that says "Add Python to PATH" before clicking "Install Now".
    - **macOS**: Use the installer package and follow the instructions.
    - **Linux**: You can usually install Python via your package manager (e.g., `sudo apt-get install python3`  for Debian-based distributions).
3. **Verify Installation**:
    - Open a terminal or command prompt.
    - Type `python --version`  (or `python3 --version`  on some systems) to check if Python is installed correctly and see the version number.
4. **Set Up a Development Environment**:
    - **IDEs and Editors**: Use an Integrated Development Environment (IDE) or a text editor that supports Python. Popular choices include:
        - **PyCharm** (IDE)
        - **Visual Studio Code** (Editor)
        - **Jupyter Notebook** (for data science and interactive computing)
    - **Virtual Environments**: Use virtual environments to manage dependencies for different projects.
        - Create a virtual environment with `python -m venv myenv`  and activate it with `source myenv/bin/activate`  (Unix) or `myenv\Scripts\activate`  (Windows).
**Running Your First Python Program**

1. **Create a Python File**:
    - Open your text editor or IDE.
    - Create a new file named `hello.py` .
2. **Write Your First Program**:
    - Add the following code to `hello.py` :
```python
print("Hello, World!") 
```
1. **Run the Program**:
    - Open a terminal or command prompt.
    - Navigate to the directory where `hello.py`  is located.
    - Run the program by typing `python hello.py`  (or `python3 hello.py`  on some systems).
2. **Output**:
    - You should see the `output: ` 
```python
Hello, World!  
```
