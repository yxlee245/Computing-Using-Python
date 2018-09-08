def factorial(n):
    '''recursive factorial with print to show operation.'''
    indent = 4 * (6 - n) * ' '    #  more indent on deeper recursion
    print(indent + 'Enter factorial n = ', n)
    if n == 1:    # base case
        print(indent + 'Base case.')
        return 1
    else:    # recursive case
        print(indent + 'Before recursive call f(' + str(n - 1) + ')')
        # separate recursive call allows print after call
        rest = factorial(n - 1)
        print(indent + 'After recursive call f(' + str(n-1) + ') = ', rest)
        return n * rest