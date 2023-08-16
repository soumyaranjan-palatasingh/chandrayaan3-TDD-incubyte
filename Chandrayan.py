class ChandrayanSpacecraft:
    def __init__(self, initial_position, initial_direction):
        self.position = initial_position
        self.direction = initial_direction
        
    def move_forward(self):
        if self.direction == 'N':
            self.position[1] += 1
        elif self.direction == 'S':
            self.position[1] -= 1
        elif self.direction == 'E':
            self.position[0] += 1
        elif self.direction == 'W':
            self.position[0] -= 1
        elif self.direction == 'Up':
            self.position[2] += 1
        elif self.direction == 'Down':
            self.position[2] -= 1

    def move_backward(self):
        if self.direction == 'N':
            self.position[1] -= 1
        elif self.direction == 'S':
            self.position[1] += 1
        elif self.direction == 'E':
            self.position[0] -= 1
        elif self.direction == 'W':
            self.position[0] += 1
        elif self.direction == 'Up':
            self.position[2] -= 1
        elif self.direction == 'Down':
            self.position[2] += 1
    
    
    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def turn_up(self):
        if self.direction == 'N' or self.direction == 'S':
            self.direction = 'Up'

    def turn_down(self):
         if self.direction == 'N' or self.direction == 'S':
            self.direction = 'Down'