## Homework 1

Extract car names from this text.

txt = 'MsaatmiazD'

## Homework 2

Extract residence are from this text.

txt = "I'am John. I am from London"

Homework_1
txt='MsaatmiazD'
txt[::2]
txt[-1::-2]

#homework_2

txt = "I'am John. I am from London"
residence = txt.split('from ')[-1]
residence
