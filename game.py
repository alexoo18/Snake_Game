# Main Game class that orchestrates all game components

import pygame
import sys
from constants import *
from snake import Snake
from food import Food
from renderer import Renderer
from input_handler import InputHandler


class Game:
    # Main game class that manages game state and coordinates all components
    
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        
        # Create screen and set up display
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        
        # Create game components
        self.clock = pygame.time.Clock()
        self.renderer = Renderer(self.screen)
        self.input_handler = InputHandler()
        
        # Initialize game state
        self.reset_game()
    
    def reset_game(self):
        # Reset the game to initial state
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False
        self.paused = False
        
        # Make sure food doesn't spawn on snake
        self.food.respawn(self.snake.get_all_positions())
    
    def update_game_logic(self):
        # Update game logic - only when not paused 
        if self.game_over or self.paused:
            return
        
        # Move snake
        self.snake.move()
        
        # Check food collision
        if self.food.is_eaten_by(self.snake.get_head_position()):
            self.snake.grow()
            self.score += SCORE_PER_FOOD
            self.food.respawn(self.snake.get_all_positions())
        
        # Check collisions
        if self.snake.check_collision():
            self.game_over = True
    
    def handle_input(self):
        # Handle all inputs 
        if not self.input_handler.handle_events():
            return False
        
        # Handle pause
        if self.input_handler.is_pause_requested() and not self.game_over:
            self.paused = not self.paused
        
        # Handle restart
        if self.input_handler.is_restart_requested() and self.game_over:
            self.reset_game()
        
        # Handle movement (only when game is active)
        if not self.paused and not self.game_over:
            direction = self.input_handler.get_direction_input()
            if direction:
                self.snake.change_direction(direction)
        
        return True
    
    def render_frame(self):
        # Clear screen
        self.renderer.clear_screen()

        # Draw UI background bar
        self.renderer.draw_ui_background()

        # Draw play area border
        self.renderer.draw_grid()
        
        # Draw snake (alive or dead)
        if self.game_over:
            self.renderer.draw_snake(self.snake, dead=True, flash=True)
        else:
            self.renderer.draw_snake(self.snake)

        # Draw food only if the game is active
        if not self.game_over:
            self.renderer.draw_food(self.food)
        
        # Draw UI elements
        self.renderer.draw_score(self.score, self.snake.get_length())
        self.renderer.draw_controls()
        
        # Overlays (pause / game over)
        if self.paused and not self.game_over:
            self.renderer.draw_pause_screen()
        elif self.game_over:
            self.renderer.draw_game_over(self.score, self.snake.get_length())
        
        # Update display
        self.renderer.update_display()
    
    def run(self):
        # Main game loop
        print("Starting Snake Game...")
        print("Controls: Arrow Keys/WASD to move, P to pause, ESC to quit")
        
        running = True
        while running:
            running = self.handle_input()
            self.update_game_logic()
            self.render_frame()
            self.clock.tick(GAME_SPEED)
        
        print("Game ended. Thank you for playing!")
        pygame.quit()
        sys.exit()
    
    def get_game_stats(self):
        # Get current game statistics
        return {
            'score': self.score,
            'snake_length': self.snake.get_length(),
            'game_over': self.game_over,
            'paused': self.paused,
            'snake_position': self.snake.get_head_position(),
            'food_position': self.food.get_position()
        }
