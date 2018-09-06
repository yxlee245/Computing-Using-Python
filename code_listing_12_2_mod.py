class MyClass(object):
    def __init__(self, param1=0):
        '''constructor, sets attribute value to
        param1, default is 0'''
        print('in constructor')
        self.value = param1

    def __str__(self):
        '''Convert val attribute to string.'''
        print('in str')
        return 'Val is: {}'.format(str(self.value))

    def __add__(self, param2):
        '''Perform addition with param2, a MyClass instance.
        Return a new My Class instance with sum as value attribute'''
        print('in add')
        result = self.value + param2.value
        return MyClass(result)

# testing the class
inst1 = MyClass(27)
print(type(inst1))
print(type(MyClass))
print(inst1)
a_sum = inst1 + inst1
print(a_sum)
print(type(a_sum))