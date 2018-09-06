class NewClass(object):
    def __init__(self, attribute='default', name='Instance'):
        self.name = name    # public attribute
        self.__attribute__ = attribute    # a 'private' attribute
    def __str__(self):
        return '{} has attribute {}'.format(self.name, self.__attribute__)

# testing out the class
inst1 = NewClass(name='Monty', attribute='Python')
print(inst1)
print(inst1.name)
print(inst1.__attribute__)