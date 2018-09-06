import math    # need sqrt (square root)

# a Point is a Cartesian point (x, y)
# all values are float unless otherwise stated
class Point(object):
    def __init__(self, x_param=0.0, y_param=0.0):
        '''Create x and y attributes. Defaults are 0.0'''
        self.x = x_param
        self.y = y_param

    def distance(self, param_pt):
        '''Distance between self and a Point'''
        x_diff = self.x - param_pt.x
        y_diff = self.y - param_pt.y
        # square differences, sum and take sqrt
        return math.sqrt(x_diff ** 2 + y_diff ** 2)
    
    def sum(self, param_pt):
        '''Vector Sum of self and a Point
        return a Point instance'''
        # new_pt = Point()
        # new_pt.x = self.x + param_pt.x
        # new_pt.y = self.y + param_pt.y
        return Point(self.x + param_pt.x, self.y + param_pt.y)
    
    def __str__(self):
        '''Print as a coordinate pair.'''
        # print('called the __str__ method')
        return '({:.2f}, {:.2f})'.format(self.x, self.y)

# trying out certain values
origin = Point()
point1 = Point(1, 0)
point2 = Point(0, 1)
point3 = Point(1, 1)

print('Distances from origin to')
print('  point 1:', origin.distance(point1))
print('  point 2:', origin.distance(point2))
print('  point 3:', origin.distance(point3))

print()

print('Vector Sums of')
print('  points 1 and 2', point1.sum(point2))
print('  points 1 and 3', point1.sum(point3))
print('  points 2 and 3', point2.sum(point3))