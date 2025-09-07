import random
from constants import GRID_WIDTH, GRID_HEIGHT

# this class handles the food placement and respawning 
class Food:
    def __init__(self):
        # places food in random location 
        self.position = self._generate_random_position()
        self.eaten = False

    def _generate_random_position(self):
        # generates a random location within the grid
        x = random.randint(0, GRID_WIDTH - 2)
        y = random.randint(0, GRID_HEIGHT - 2)
        return (x, y)
    
    def get_position(self):
        # get the current position of the food 
        return self.position
    
    def respawn(self, occupied_positions = None):
        # respawn the food at a random postion 
        if occupied_positions is None:
            occupied_positions = []

        # keep generating new position until one not occupied
        # is found 
        max_attempts = 100 #preventing infinite loop in edge cases
        attempts = 0

        while attempts < max_attempts:
            new_position = self._generate_random_position()
            if new_position not in occupied_positions:
                self.position = new_position
                self.eaten = False
                return
            attempts += 1

        # if there is no empty spot, place randomly
        self.position = self._generate_random_position()
        self.eaten = False

    def is_eaten_by(self, position):
        # check if the food is eaten at the given postion 
        # position of the (x, y) location to compare with the food
        # return true if the positon matches, if not false
        if position == self.position and not self.eaten:
            self.eaten = True
            return True 
        return False
    
    def reset(self):
        # reset the food to a new random position 
        self.position = self._generate_random_position()
        self.eaten = False
