# recursive function to reverse a string

def reverse(a_str):
    '''Recursive function to reverse a string.'''
    print('Got as an argument:', a_str)
    # base case
    if len(a_str) == 1:
        print('Base Case!')
        return a_str
    # recursive step
    else:
        new_str = reverse(a_str[1:]) + a_str[0]
        print('Reassembling {} and {} into {}'.format(a_str[1:], a_str[0], new_str))
        return new_str

the_str = input('Reverse what string: ')
result = reverse(the_str)
print('The reverse of {} is {}'.format(the_str, result))