# Renderer class for the graphics 

import pygame
from constants import *


# handles all drawing and rendering operations 
class Renderer:
    def __init__(self, screen):
        # initialise the graphics 
        self.screen = screen
        self.font_small = pygame.font.SysFont("Aptos", 24)
        self.font_medium = pygame.font.SysFont("Aptos", 36)
        self.font_large = pygame.font.SysFont("Aptos", 72)
    
    def clear_screen(self):
        # Fill screen with background color
        self.screen.fill(BLACK)
    
    def draw_grid(self):
        # Draw only the outer boundary of the play area
        play_area = pygame.Rect(0, UI_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT - UI_HEIGHT)
        pygame.draw.rect(self.screen, GRAY, play_area, 2) 
    
    def draw_snake(self, snake, dead=False, flash=False):
        # Draw the snake (alive or dead look)
        positions = snake.get_all_positions()

        # Flashing color logic
        if dead and flash:
            flash_color = RED if pygame.time.get_ticks() // 200 % 2 == 0 else BLACK

        for i, (x, y) in enumerate(positions):
            pixel_x = x * GRID_SIZE
            pixel_y = y * GRID_SIZE + UI_HEIGHT
            center = (pixel_x + GRID_SIZE // 2, pixel_y + GRID_SIZE // 2)
            radius = GRID_SIZE // 2 - 2

            if i == 0:  # Head
                if dead:
                    color = flash_color if flash else RED
                    border = (200, 0, 0)
                    pygame.draw.circle(self.screen, color, center, radius)
                    pygame.draw.circle(self.screen, border, center, radius, 2)

                    # X eyes
                    eye_offset_x = 6
                    eye_offset_y = -3
                    left_eye = (center[0] - eye_offset_x, center[1] + eye_offset_y)
                    right_eye = (center[0] + eye_offset_x, center[1] + eye_offset_y)
                    for eye in [left_eye, right_eye]:
                        pygame.draw.line(self.screen, WHITE, (eye[0]-3, eye[1]-3), (eye[0]+3, eye[1]+3), 2)
                        pygame.draw.line(self.screen, WHITE, (eye[0]-3, eye[1]+3), (eye[0]+3, eye[1]-3), 2)
                else:
                    # Alive head
                    pygame.draw.circle(self.screen, DARK_GREEN, center, radius)
                    pygame.draw.circle(self.screen, GREEN, center, radius, 2)

                    # Eyes
                    eye_radius = 3
                    eye_offset_x = 5
                    eye_offset_y = -3
                    eye1 = (center[0] - eye_offset_x, center[1] - eye_offset_y)
                    eye2 = (center[0] + eye_offset_x, center[1] - eye_offset_y)
                    pygame.draw.circle(self.screen, WHITE, eye1, eye_radius)
                    pygame.draw.circle(self.screen, WHITE, eye2, eye_radius)
            else:  # Body
                if dead:
                    color = flash_color if flash else (139, 0, 0)
                    border = (200, 0, 0)
                    pygame.draw.circle(self.screen, color, center, radius)
                    pygame.draw.circle(self.screen, border, center, radius, 1)
                else:
                    pygame.draw.circle(self.screen, GREEN, center, radius)
                    pygame.draw.circle(self.screen, DARK_GREEN, center, radius, 1)      
    
    def draw_food(self, food):
        x, y = food.get_position()
        pixel_x = x * GRID_SIZE
        pixel_y = y * GRID_SIZE + UI_HEIGHT
    
        center = (pixel_x + GRID_SIZE // 2, pixel_y + GRID_SIZE // 2)
        radius = GRID_SIZE // 2 - 2

        pygame.draw.circle(self.screen, RED, center, radius)   # Apple body
        pygame.draw.circle(self.screen, WHITE, center, radius, 2)  # Border

        # Stem
        stem_rect = pygame.Rect(center[0] - 2, center[1] - radius - 4, 4, 6)
        pygame.draw.rect(self.screen, (139, 69, 19), stem_rect)
        # Leaf
        leaf_rect = pygame.Rect(center[0] + 2, center[1] - radius - 2, 6, 4)
        pygame.draw.ellipse(self.screen, GREEN, leaf_rect)

    def draw_ui_background(self):
        ui_bar = pygame.Rect(0, 0, WINDOW_WIDTH, UI_HEIGHT)
        pygame.draw.rect(self.screen, (30, 30, 30), ui_bar)  # dark gray bar
    
    def draw_score(self, score, snake_length):
        score_text = self.font_medium.render(f"Score: {score}", True, WHITE)
        length_text = self.font_medium.render(f"Length: {snake_length}", True, WHITE)
        self.screen.blit(score_text, (10, 20))
        self.screen.blit(length_text, (10, 50))
    
    def draw_controls(self):
        controls = [
            "Use Arrow Keys to move",
            "P - Pause",
            "ESC - Quit"
        ]
        for i, text in enumerate(controls):
            control_text = self.font_small.render(text, True, WHITE)
            self.screen.blit(control_text, (WINDOW_WIDTH - 200, 20 + i * 25))
    
    def draw_pause_screen(self):
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        pause_text = self.font_large.render("PAUSED", True, YELLOW)
        text_rect = pause_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.screen.blit(pause_text, text_rect)
        
        resume_text = self.font_medium.render("Press P to resume", True, WHITE)
        resume_rect = resume_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        self.screen.blit(resume_text, resume_rect)
    
    def draw_game_over(self, final_score, snake_length):
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        game_over_text = self.font_large.render("GAME OVER!", True, RED)
        game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100))
        self.screen.blit(game_over_text, game_over_rect)
        
        score_text = self.font_medium.render(f"Final Score: {final_score}", True, WHITE)
        score_rect = score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 40))
        self.screen.blit(score_text, score_rect)
        
        length_text = self.font_medium.render(f"Final Length: {snake_length}", True, WHITE)
        length_rect = length_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.screen.blit(length_text, length_rect)
        
        restart_text = self.font_medium.render("Press SPACE to restart", True, YELLOW)
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60))
        self.screen.blit(restart_text, restart_rect)
        
        quit_text = self.font_medium.render("Press ESC to quit", True, WHITE)
        quit_rect = quit_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100))
        self.screen.blit(quit_text, quit_rect)
    
    def update_display(self):
        pygame.display.flip()
