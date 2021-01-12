##################################################################
## if ... elif ... else Statements
## Execute a specific block of code if a condition is evaluated to True
##################################################################

a, b = 3, 5
if a < b:  # if a is less that b execute the indented block of code under the if clause, otherwise go and test the elif condition
    print('a is less than b')
elif a == b:  # if a is equal to b execute the indented block of code that fallows, otherwise execute the block of code under the else clause
    print('a is equal to b')
else:
    print('a is greater than b')

## or / and operators
your_age = 14
if your_age < 0 or your_age > 99:  # if ANY of the expression is True execute the indented block of code under the if clause
    print('Invalid age!')
elif your_age <= 2:
    print('You are an Infant')
elif your_age < 18:
    print('You are a child')
else:
    print('You are an adult')

a = 3
if 1 < a <= 9:
    print('a is greater than 1 and less than of equal to 9')

# equivalent to
if a > 1 and a <= 9:
    print('a is greater than 1 and less than of equal to 9')

a = 12
## The fallowing 3 exemples test if a number a is divisible by 6
## 1st Example - nested if
if a % 2 == 0:
    if a % 3 == 0:
        print('Example 1: a is divisible by 2 and 3 (or by 6)')

## 2nd Example: and operator -> it returns True if both expressions are True, False otherwise
if a % 2 == 0 and a % 3 == 0:
    print('Example 2: a is divisible by 2 and 3 (or by 6)')

## 3rd Example
if not (a % 2 and a % 3):  # the truthniness of an expression: a % 2 is equal to bool(a %2)
    print('Example 2: a is divisible by 2 and 3 (or by 6)')

## The truthiness of a variable
b = 0
if b:  # it test the truthiness of b or bool(b)
    print('The truthiness of b: True')
else:
    print('The truthiness of b: False')

my_str = 'some string'
if my_str:  # it test the truthiness of my_str or bool(my_str)
    print('The truthiness of my_str: True')
else:
    print('The truthiness of my_str: False')

name = 'Andrei'
## Pythonic version
print('Hello Andrei') if name == 'Andrei' else print('You are not Andrei!')

# equivalent to:
if name == 'Andrei':
    print('Hello Andrei')
else:
    print('You are not Andrei')

#################################
## For Loops and Ranges
#################################

movies = ['Star Wars', 'The Godfather', 'Harry Potter ', 'Lord of the Rings']

for m in movies:  # it iterates over a sequence and executes the code indented under the "for" clause for each element in the sequence
    print(f'One of my favorites movie is {m}')
else:  # the indented code below "else" will be executed when "for" has finished looping over the entire list (no "break" statement executed)
    print('This is the end of the list')

for i in range(100):
    pass  # => empty instruction or "no nothing"

for i in range(10):  # => from 0 (default, included) to 10 excluded
    print(i, end=' ')
# it prints:  0 1 2 3 4 5 6 7 8 9

for i in range(3, 9):  # => from 3 included to 9 excluded
    print(i, end=' ')
# it prints: 3 4 5 6 7 8


for i in range(3, 20, 3):  # => from 3 included to 20 excluded in steps of 3
    print(i, end=' ')
# it prints: 3 6 9 12 15 18


for i in range(8, -4, -2):  # => from 8 included to -4 excluded in steps of -2
    print(i, end=' ')
# it prints: 8 6 4 2 0 -2


## for ... continue -> it prints all letters of the string without 'o'
for letter in 'Python Go and Java Cobol':
    if letter == 'o':
        continue  # go to the beginning of the for loop and do the next iteration
    print(letter, end='')

## for ... break
sequence = [1, 5, 19, 3, 31, 100, 55, 34]
for item in sequence:
    if item % 17 == 0:
        print('A number divisible by 17 has been found! Breaking the loop...')
        break  # breaks out of the loop (executes the first instruction (if any) after the else block of code)
else:
    print('There is no number divisible by 17 in the sequence')

#################################
## While Loops
#################################

a = 10
## Infinite Loop, it prints 10 indefinitely

# while a:  #it tests the truthiness of a or bool(a) which is always True
#    print(a)

## Prints numbers from 10 to 1
while a:  # => "while a:" is equivalent to "while a > 0:"
    print(a)
    a -= 1
else:  # => executes the below block of code after finishing the while looop (and if no "break" statement has been executed)
    print('Finishing printing numbers. a is now 0')

## it prints only odd numbers between 1 and 20
a = 0
while a < 20:
    a += 1
    if a % 2 == 0:
        continue  # go the the beginning of the while loop
    print(f'Odd number {a}')  # it reaches this line only if the continue statement hasn't been executed

## it prints numbers greater than 2
a = 7
while a > 0:
    a -= 1
    if a == 2:
        break  # => it breaks out of the while loop and executes the next instruction after the while block of code
    print(a)

print('Loop ended.')

