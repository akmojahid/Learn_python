# 1. Printing a message
print("Hello, World!")  # Output: Hello, World!

# 2. Variables and data types
x = 5  # integer
y = 3.14  # float
name = "Mojahid"  # string
is_student = True  # boolean

# 3. Basic arithmetic operations
sum = x + y  # addition
difference = x - y  # subtraction
product = x * y  # multiplication
quotient = x / y  # division
remainder = x % y  # modulus (remainder of division)

# 4. Lists
fruits = ["apple", "banana", "cherry"]  # list of fruits
first_fruit = fruits[0]  # accessing first element
fruits.append("orange")  # adding an element to the list

# 5. Tuples
coordinates = (10, 20)  # tuple with two elements
x_coord = coordinates[0]  # accessing first element

# 6. Dictionaries
person = {
    "name": "Mojahid",
    "age": 25,
    "city": "Dhaka"
}
name = person["name"]  # accessing value by key
person["email"] = "mojahid@example.com"  # adding a new key-value pair

# 7. Conditional statements
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

# 8. Loops
# for loop
for fruit in fruits:
    print(fruit)  # prints each fruit in the list

# while loop
count = 0
while count < 5:
    print("Count:", count)  # prints the current count
    count += 1  # increment the count by 1

# 9. Functions
def greet(name):
    return "Hello, " + name

message = greet("Mojahid")  # calling the function with "Mojahid"

# 10. Classes and objects
class Dog:
    def __init__(self, name, breed):
        self.name = name  # instance variable
        self.breed = breed  # instance variable
    
    def bark(self):
        return self.name + " says Woof!"

my_dog = Dog("Rex", "German Shepherd")  # creating an object of class Dog
print(my_dog.bark())  # Output: Rex says Woof!