# Generate a hailstone sequence
number_str = input('Enter a positive integer: ')
number = int(number_str)
count = 0

print('Starting with number:', number)
print('Sequence is: ', end=' ')

while number > 1:    # stop when the sequence reaches 1

    if number % 2:    # number is odd
        number = number * 3 + 1
    else:    # number is even
        number /= 2
    print(int(number), ',', end=' ')    # add number to sequence

    count += 1    # add to the count

else:
    print()    # blank line for a nicer output
    print('Sequence is', count, 'numbers long')
