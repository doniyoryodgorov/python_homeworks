## Homeworks:
##Write a program that will check evennes of given number
##From given 3 numbers from input, find the biggest number
##Write a program that will find if the letter is vowel (aeiou) or consonant

## 
number=int(input("Enter a number: "))
if number%2==0:
    print('This number is even')
else:
    print('This number is odd') 

##From given 3 numbers from input, find the biggest number
a=int(input('Enter first number:'   ))
b=int(input('Enter second number:'  ))
c=int(input('Enter third number:'   ))
if a>b and a>c:
    print('The biggest number is:',a )
elif b>a and b>c:
    print('The biggest number is:',b )
else:
    print('The biggest nuber is:' ,c) 


##Write a program that will find if the number is vowel (aeiou) or consonant
letter=input('Enter a letter:   ').lower
if letter in 'auioe':
    print('This letter is a vowel')
else:
    print('This letter is a consonant')

