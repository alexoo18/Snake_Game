from constants import GRID_WIDTH, GRID_HEIGHT, RIGHT

class Snake:
    # Handles the snake's movement, growth, and collision detection

    def __init__(self):
        # Initialise the snake at the centre of the grid
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.grow_flag = False

    def move(self):
        # Move the snake in the current direction
        head_x, head_y = self.positions[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        # Add new head
        self.positions.insert(0, new_head)

        # Remove tail unless snake should grow
        if self.grow_flag:
            self.grow_flag = False
        else:
            self.positions.pop()

    def change_direction(self, new_direction):
        # Change the direction of the snake.
        # Prevents reversing directly into itself.
        opposite_direction = (-self.direction[0], -self.direction[1])
        if new_direction != opposite_direction:
            self.direction = new_direction

    def grow(self):
        # Make snake grow on the next move
        self.grow_flag = True

    def get_head_position(self):
        # Get the position of the snake's head
        return self.positions[0]

    def get_body_positions(self):
        # Get the positions of the snake's body (excluding head)
        return self.positions[1:]

    def get_all_positions(self):
        # Get the positions of the whole snake
        return self.positions

    def get_length(self):
        # Get the current length of the snake
        return len(self.positions)

    def check_wall_collision(self):
        # Check if the snake head hits the walls
        head_x, head_y = self.get_head_position()
        return (
            head_x < 0 or head_x >= GRID_WIDTH or
            head_y < 0 or head_y >= GRID_HEIGHT
        )

    def check_self_collision(self):
        # Check if the snake collided with its own body
        head = self.get_head_position()
        return head in self.get_body_positions()

    def check_collision(self):
        # Check for any collision (wall or self)
        return self.check_wall_collision() or self.check_self_collision()

    def reset(self):
        # Reset the snake to the original state
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.grow_flag = False
