Control flow in Python refers to the order in which individual statements, instructions, or function calls are executed or evaluated in a program. It includes conditional statements, loops, and functions.

# 1. Conditional Statements
These are used to execute code only if a specific condition is met.

- if, elif, else:
- if: Executes a block of code if a condition is True.
- elif: Checks another condition if the previous ones are False.
- else: Executes when none of the conditions are True.

```python3
x = 10
if x > 15:
    print("x is greater than 15")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")
```

## 2. Loops
Loops are used to execute a block of code repeatedly.

### while Loop:
Executes as long as the condition is True.

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```
### for Loop:
Iterates over a sequence (such as a list, string, or range).

```python

for i in range(1, 6):
    print(i)
3. Control Flow Tools
break:
```
Exits the loop prematurely when a condition is met.

```python

for i in range(1, 10):
    if i == 5:
        break
    print(i)
continue:
```
Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.

```python

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
pass:
```
Does nothing. It is a placeholder when a statement is required syntactically but no code needs to be executed.

```python

if x > 0:
    pass  # Placeholder for future code
else with Loops:
```
The else block in loops executes only if the loop completes without hitting a break.

```python

for i in range(1, 5):
    print(i)
else:
    print("Loop completed!")
```
