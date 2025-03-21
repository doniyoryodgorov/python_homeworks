#Task_1 Create a Dictionary from Two Lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

my_dict = dict(zip(keys,values))
my_dict

#Task_2 Find the Maximum Value in a Dictionary

scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
max_score = max(scores, key=scores.get)
max_score

# Task_3 Find the Union of Two Sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C=A.union(B)
C

# Task_4 Check if `"age"` exists in the dictionary without using a loop.

person = {"name": "John", "age": 30, "city": "London"}

if "age" in person:
    print("Key 'age' exists in the dictionary") 
else:
     print("Key 'age' doesn't exist in the dictionary") 

   

#Task_5 Get Unique Values from a Dictionary
grades = {"Alice": "A", "Bob": "B", "Charlie": "A", "David": "C"}

uni_grades = set(grades.values())

print(uni_grades)

#Task_6

pairs = [("one", 1), ("two", 2), ("three", 3)]

#Task_7

temperatures = {"Monday": 20, "Tuesday": 15, "Wednesday": 22}

m = min(temperatures.values())

d = dict(pairs)

#Task_8

X = {10, 20, 30, 40}
Y = {30, 40, 50, 60}

X.difference(Y)
