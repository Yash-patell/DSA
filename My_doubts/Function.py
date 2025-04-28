#create a function and calling it - simple

def greet():
    
    print("hello world")
    
greet() #calling the function here


# --------------creating a function and pass a value while calling----------------------------------------

def greeting(name):
    
    print(name)
    
greeting("billu")

# ---------------------------------Returning values from a function

def add_numbers(a,b):
    result = a+b
    return result


print(add_numbers(5,3))

# - -------------------------------------- calling a function inside the same class

class Calculator:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        sum_result = self.add(a, b)  # Calling 'add' method from within 'multiply' method
        return sum_result * 2

# Create an object of the class
calc = Calculator()

# Call the multiply method
result = calc.multiply(3, 4)

print(result)  # Output will be (3 + 4) * 2 = 14


#-------------- calling a method with a parameter

class hello:
    
    def hello_person(self, name):
        print(name)
        

class users:
    def call_person(self, name):
        
        hii =hello()
        hii.hello_person(name)

user = users()

user.call_person("cat")


# ------------ Instance Atrribute -------------------------------------------
# when we use self.name = name it means that the value will be saved as a part of object's state and it can be accessed  or modified later
class Person:
    def __init__(self, name):
        self.name = name  # Store the 'name' in an instance attribute
    
    def print_name(self):
        print(self.name)  # Access the instance attribute

p1 = Person("Alice")
p1.print_name()  

# ---------------------- without saving instance variable---------------------------
class Person:
    def print_name(self, name):
        print(name)  # Just prints the value temporarily, doesn't save it
    
p1 = Person()  # creating an instance of the object
p1.print_name("Alice")  # Output: Alice
