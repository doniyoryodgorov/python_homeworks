

Given two integer variables: a and b. Swap the values of the variables.
a = int(input())
b = int(input())

# write code here. Don't change given conditions

print(a, b)

Solve this problem in 3 ways

method 1

a = int(input())
b = int(input())

temp = a
a = b
b = temp

print(a, b)

method 2

a = int(input())
b = int(input())

a, b = b, a

print(a, b)

method 3

a = int(input())
b = int(input())

a = a + b
b = a - b
a = a - b

print(a, b)



