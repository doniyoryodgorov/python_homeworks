# 1 Problem: Define a class Car with attributes brand and year. Create an object and print its attributes.
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

  car1=Car('Chevrolet',2019)
print(f"Brand: {car1.brand}, Year:{car1.year}")

#Problem 2: Create a class Person with a default constructor that sets name = "John" and age = 30.
class Person:
    def __init__(self,name='John',age=30):
        self.name = name
        self.age = age

  person1=Person()
print(f"Name: {person1.name}, Age: {person1.age}")

#Problem 3: Create a class Circle with an attribute radius and a method area() that returns the area of the circle.
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print("Area of the circle is: ",3.14*self.radius*self.radius)     

circle1=Circle(5)
print("Area of the circle is: ",circle1.area())

#Problem 4: Define a class Rectangle with methods area() and perimeter().
class Retangle:
    def __init__ (self,length,width):
        self.length = length
        self.width = width
    def area(self):
        print("Area of the rectangle is: ",self.length*self.width)
    def perimeter(self):
        print("Perimeter of the rectangle is: ",2*(self.length+self.width)) 

Retangle1=Retangle(10,6)
Retangle1.area() 
Retangle1.perimeter() 

#Problem 5: Create a class BankAccount with a private attribute _balance. Provide methods to deposit and withdraw money.
class BankAccount:
    def __init__(self):
        self._balance = 0
    def deposit(self,amount):
        self._balance += amount
    def withdraw(self,amount):
        if amount > self._balance:
            print("Insufficient balance")
        else:
            self._balance -= amount
    def display(self):
        print("Balance: ",self._balance)

#6 Problem: Create a class method that will add x to y. Show the output
class add:
    def __init__(self):
        pass                        
    def add(x,y):
        return x+y

#7 Problem: Create classes A and B. Create a class C that inherits from both
class A:
    def __init__(self):
        print("Initializing A")

class B:
    def __init__(self):
        print("Initializing B")

class C(A, B):
    def __init__(self):
        super().__init__()  # Bu faqat birinchi parent klassning __init__ funksiyasini chaqiradi
        print("Initializing C")

# Sinflarni chaqirish
c_instance = C()


#Problem 8: Create a class Secret with a private method _hidden_message() that prints "This is private".
class Secret:
    def __hidden_message(self):
        return "This is private"

    def access_hidden_message(self):
        return self.__hidden_message()

# Creating an object
sec = Secret()

# Accessing private method via a public method
print(sec.access_hidden_message())

#Problem_9: Create a class Student that keeps track of the total number of students created
class Student:
    count = 0  # Class variable to count students

    def __init__(self, name):
        self.name = name
        Student.count += 1  # Increment counter

# Creating objects
s1 = Student("Alice")
s2 = Student("Bob")

# Printing total students
print(f"Total Students: {Student.count}")

#Problem_10: Create a class EvenNumbers that generates even numbers up to a given limit using a method generate_even().

class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit

    def generate_even(self):
        for num in range(0, self.limit + 1, 2):
            yield num

# Creating an object
evens = EvenNumbers(10)

# Printing even numbers
print(list(evens.generate_even()))






