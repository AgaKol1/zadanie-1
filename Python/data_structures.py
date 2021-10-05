# Integer data type
a = 1
print(a)
print(type(a))

# Numeric data type
b = 1.0
print(b)
print(type(b))

# String (text) data type
c = "ABC" # Double quotes required!
print(c)
print(type(c))

# List data type
d = [1, 2, 3, 4] 
f = ["a", "b", "c"] #square brackets required

print(d)
print(type(d))

print(f)
print(type(f))

# Dictionary data type
g = {"name": "Adam",
     "surname": "Smith",
     "age": 20,
     "city": "New York"}

print(g)
print(type(g)) 

# print() and type() are functions - similar to functions in Excel
     
#########################
# More Advanced Example #
#########################

class Person:
    def __init__(self, name=None, surname=None, age=None):
        self.name = name
        self.surname = surname
        self.age = age

new_person = Person("Adam", "Smith", 20)

print(new_person.name, new_person.surname, new_person.age)
print(type(new_person))

input() # waiting for user input to not close terminal
