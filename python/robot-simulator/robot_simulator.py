# Globals for the directions
# Change the values as you see fit
EAST = 1
NORTH = 0
WEST = 3
SOUTH = 2

class Robot:

    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.coordinates = (x, y)

    def move(self, sequence):
        for step in sequence:
            if step == 'R':
                self.direction = (self.direction + 1) % 4
            elif step == 'L':
                self.direction = (self.direction - 1) % 4
            elif step == 'A':
                self.advance()
            else:
                raise ValueError('Invalid sequence move')

    def advance(self):
        if self.direction == NORTH:
            self.coordinates = self.coordinates[0], self.coordinates[1] + 1
        elif self.direction == SOUTH:
            self.coordinates = self.coordinates[0], self.coordinates[1] - 1
        elif self.direction == EAST:
            self.coordinates = self.coordinates[0] + 1, self.coordinates[1]
        elif self.direction == WEST:
            self.coordinates = self.coordinates[0] - 1, self.coordinates[1]
