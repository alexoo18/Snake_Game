# handler class for the Snake game


import pygame
from constants import UP, DOWN, LEFT, RIGHT

class InputHandler:
    # Handles all keyboard input and events
    
    def __init__(self):
        # Initialize input handler
        self.quit_requested = False
        self.pause_requested = False
        self.restart_requested = False
        self.direction_requested = None
    
    def handle_events(self):
        # Process all pygame events
        # Reset single-frame events
        self.pause_requested = False
        self.restart_requested = False
        self.direction_requested = None
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_requested = True
                return False
            
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event.key)
        
        return not self.quit_requested
    
    def _handle_keydown(self, key):
        # Handle keydown events
        # Movement keys
        if key in [pygame.K_UP, pygame.K_w]:
            self.direction_requested = UP
        elif key in [pygame.K_DOWN, pygame.K_s]:
            self.direction_requested = DOWN
        elif key in [pygame.K_LEFT, pygame.K_a]:
            self.direction_requested = LEFT
        elif key in [pygame.K_RIGHT, pygame.K_d]:
            self.direction_requested = RIGHT
        
        # Control keys
        elif key == pygame.K_p:
            self.pause_requested = True
        elif key == pygame.K_SPACE:
            self.restart_requested = True
        elif key == pygame.K_ESCAPE:
            self.quit_requested = True
    
    def get_direction_input(self):
        # Get the requested direction change
        return self.direction_requested
    
    def is_pause_requested(self):
        # Check if pause was requested this frame
        return self.pause_requested
    
    def is_restart_requested(self):
        # Check if restart was requested this frame
        return self.restart_requested
    
    def is_quit_requested(self):
        # Check if quit was requested 
        return self.quit_requested
    
    def reset_requests(self):
        # Reset all request flags 
        self.quit_requested = False
        self.pause_requested = False
        self.restart_requested = False
        self.direction_requested = None