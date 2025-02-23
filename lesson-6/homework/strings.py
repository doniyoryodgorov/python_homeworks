#Task_1 
#Reverse given string using for loop

text = "Hello World"
reversed_text = ""

for char in text[::-1]:
    reversed_text += char

print("Reversed string:", reversed_text)


#Task_2

Count Vowels in a String

Problem:
Count the number of vowels (a, e, i, o, u) in a given string.

text = "Hello World"

# Output: 3

text = "Hello World"

vowels = "aeiouAEIOU"

vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)


#Task_3

Find the Maximum Number in a List

Problem:
Find the maximum number in a list using a loop (without using max()).

numbers = [5, 3, 8, 2, 9, 4]



# Output: 9

numbers = (5, 3, 8, 2, 9, 4)
count=0
for x in numbers:
    print(max(numbers))
    count<2
    break




 
