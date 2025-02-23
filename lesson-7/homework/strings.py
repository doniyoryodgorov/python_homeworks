#No Parameters / No Return Value
#	1. Write a function `greet()` that prints 'Hello, World!' when called.

def greet():
    print('Hello, world')
greet()    

#•	2. Create a function `show_date_time()` that prints the current date and time.
import datetime
def show_date_time():
    print('Current date and time is: ', datetime.datetime.now())
show_date_time()

#•	3. Write a function `display_even_numbers()` that prints even numbers from 1 to 20.
def display_even_numbers():
    print('Even numbers from 1 to 20 are: ')
    for i in range(1,21):
            if i%2==0:
                print(i) 
display_even_numbers()            

#•	4. Write a function `greet_user(name)` that takes a name as a parameter and prints 'Hello, [name]!'
def greet_user(name):
    print('Hello,', name)
greet_user('Doni')

#	5. Create a function `print_square(n)` that prints the square of a given number.
def print_square(n):
    print('Square of', n, 'is',n*n)
print_square(5)   

#•	6. Write a function `multiply_numbers(a, b)` that takes two numbers and prints their product.
def multiply_numbers(a,b):
    print('Product of', a, 'and', b, 'is', a*b)
multiply_numbers(10,9)

#•	7. Write a function `get_pi()` that returns the value of π (3.14159).
def get_pi():
    return 3.1416
get_pi()

#Create a function `random_number()` that returns a random number between 1 and 100.
def random_nuber():
    import random
    return random.randint(1,100)
random_nuber()
    
#•	9. Write a function `current_year()` that returns the current year.
import datetime
def current_year():
    return datetime.datetime.now().year
current_year()

#•	10. Write a function `add_numbers(a, b)` that returns the sum of two numbers.
def add_numbers(a,b):
    return a+b
add_numbers(10,20)

#•	11. Create a function `is_even(n)` that returns `True` if the number is even and `False` otherwise.
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
is_even(9)    

#•	12. Write a function `get_factorial(n)` that returns the factorial of a given number.
def get_factorial(n):
    fact=1                  
    for i in range(1,n+1):
        fact=fact*i
    return fact
get_factorial(4)

#•	13. Write a recursive function `countdown(n)` that prints numbers from `n` to `1`.
def countdown(n):
    if n==0:
        return 0
    else:
        print(n)
        return countdown(n-1)
countdown(5)    

#•	14. Create a recursive function `sum_natural(n)` that returns the sum of the first `n` natural numbers.
def sum_natural(n):
    if n==0:
        return 0
    else:
        return n+sum_natural(n-1)
sum_natural(4)

