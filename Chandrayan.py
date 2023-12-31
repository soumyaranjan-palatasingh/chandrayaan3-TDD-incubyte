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
    
    def execute_commands(self, commands):
        for command in commands:
            if command == 'f':
                self.move_forward()
            elif command == 'b':
                self.move_backward()
            elif command == 'l':
                self.turn_left()
            elif command == 'r':
                self.turn_right()
            elif command == 'u':
                self.turn_up()
            elif command == 'd':
                self.turn_down()

# Initial Position: (0, 0, 0)
# Initial Direction: N
initial_position = [0, 0, 0]
initial_direction = 'N'
commands = ["f", "r", "u", "b", "l"]

spacecraft = ChandrayanSpacecraft(initial_position, initial_direction)
spacecraft.execute_commands(commands)

print("Final Position:", tuple(spacecraft.position))
print("Final Direction:", spacecraft.direction)
