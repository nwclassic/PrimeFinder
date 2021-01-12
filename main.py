# This is a sample Python script.
y = 1000

y_original = y
prime_numbers = [1]

print("Let's find the primes between 1 and :", y)
print('---------------------------')

while y > 1:
    x = y // 2 + 1
    print(f'y has the value: {y}')
    print(f'x has the value: {x}')

    while x > 1:
        if y % x == 0:
            print(x, 'is a factor of ', y, '')
            print(f":-(  {y} is not a prime number.\n")
            print('---------------------------')
            break
        else:
            print(f'{x} is not a factor of {y}')
        x -= 1
    else:
        print(f'>>>>>>>>>>  {y} is prime!  <<<<<<<<<<')
        prime_numbers.insert(1,y)
        print('---------------------------\n')
    y -= 1
print(f'The primes between 1 and {y_original} are:')
for prime_num in prime_numbers:
    print(prime_num)
print(f'There are {len(prime_numbers)} primes between 1 and {y_original}')
