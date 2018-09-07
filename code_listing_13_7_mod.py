import random

class Island(object):
    '''Island
    n X n grid where zero value indicates an unoccupied cell.'''
    def  __init__(self, n, prey_count=0, predator_count=0):
        '''Initialize cell to all 0's, then fill with animals
        '''
        #print(n, prey_count, predator_count)
        self.grid_size = n
        self.grid = []
        for i in range(n):
            row = [0] * n    # row is a list of n zeros
            self.grid.append(row)
        self.init_animals(prey_count, predator_count)

    def animal(self, x, y):
        '''Return animal at location (x, y)'''
        if 0 <= x <= self.grid_size and 0 <= y <= self.grid_size:
            return self.grid[x][y]
        else:
            return -1    # outside island boundary

    def init_animals(self, prey_count, predator_count):
        '''Put some initial animals on the island
        '''
        count = 0
        # while loop continues until prey_count unoccupied positions are found
        while count < prey_count:
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)
            if not self.animal(x, y):
                new_prey = Prey(island=self, x=x, y=y)
                count += 1
                self.register(new_prey)
        count = 0
        # same while loop but for predator_count
        while count < predator_count:
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)
            if not self.animal(x, y):
                new_predator = Predator(island=self, x=x, y=y)
                count += 1
                self.register(new_predator)

    def size(self):
        '''Return size of the island: one dimension.
        '''
        return self.grid_size

    def register(self, animal):
        '''Register animal with island, i.e., put it at the
        animal's coordinates
        '''
        x = animal.x
        y = animal.y
        self.grid[x][y] = animal

    def remove(self, animal):
        '''Remove animal at its current spot'''
        x = animal.x
        y = animal.y
        self.grid_size[x][y] = 0

    def __str__(self):
        '''String representation for printing.
        (0, 0) will be in the lower-left corner.
        '''
        s = ''
        for j in range(self.grid_size-1, -1, -1):    # print row size - 1 first
            for i in range(self.grid_size):    # each row starts at 0
                if not self.grid[i][j]:
                    # print a '.' for an empty space
                    s += '{:<2s}'.format('.' + ' ')
                else:
                    s += '{:<2s}'.format((str(self.grid[i][j])) + ' ')
            s += '\n'
        return s

class Animal(object):
    def __init__(self, island, x=0, y=0, s='A'):
        '''Initialize the animals and their positions
        '''
        self.island = island
        self.name = s
        self.x = x
        self.y = y

    def position(self):
        '''Return coordinates of current position.'''
        return self.x, self.y

    def move(self):
        '''Move to an open, neighboring position.'''
        # neighbor offsets
        offset = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        for i in range(len(offset)):
            x = self.x + offset[i][0]    # neighboring coordinates
            y = self.y + offset[i][1]
            if self.island.animal(x, y) == 0:    # neighboring spot is open
                self.island.remove(self)    # remove from current spot
                self.x = x    # new coordinates
                self.y = y
                self.island.register(self)    # register new coordinates
                break    # finished with move
    
    def __str__(self):
        return self.name

class Prey(Animal):
    def __init__(self, island, x=0, y=0, s='O'):
        Animal.__init__(self, island, x, y, s)

class Predator(Animal):
    def __init__(self, island, x=0, y=0, s='X'):
        Animal.__init__(self, island, x, y, s)

def main():
    # initialization of the simulation
    royale = Island(5, 1, 1)    # 5 x 5 island, 1 predator, 1 prey
    time_steps = 20

    # run the event loop
    island_size = royale.size()
    count = 0
    while count < time_steps:
        print(royale)    # print the island
        for x in range(island_size):
            for y in range(island_size):
                animal = royale.animal(x, y)
                if animal:
                    animal.move()
        count += 1