import pygame
from pygame.locals import *

class DifficultyMenu:
    def __init__(self, window, window_width, window_height):
        """
        Initialize the DifficultyMenu object.

        Args:
            window (pygame.Surface): The window surface to render the menu on.
            window_width (int): The width of the window.
            window_height (int): The height of the window.
        """
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.font = pygame.font.Font(None, 36) 
        self.selected_difficulty = None 
        self.text_easy_rect = None
        self.text_hard_rect = None

    def display_menu(self):
        """
        Displays the difficulty menu on the game window.

        This method fills the window with a black color and renders the text for the difficulty options (Easy and Hard).
        The text is centered on the window and displayed using the specified font and color.
        The updated window is then displayed on the screen.

        Args:
            None

        Returns:
            None
        """
        self.window.fill((0, 0, 0)) # Fill the window with black color
        text_easy = self.font.render("Easy", True, (255, 255, 255))
        text_hard = self.font.render("Hard", True, (255, 255, 255))
        self.text_easy_rect = text_easy.get_rect(center=(self.window_width // 2, self.window_height // 2 - 50)) # Center the text
        self.text_hard_rect = text_hard.get_rect(center=(self.window_width // 2, self.window_height // 2 + 50)) 
        self.window.blit(text_easy, self.text_easy_rect)
        self.window.blit(text_hard, self.text_hard_rect)
        pygame.display.update()

    def select_difficulty(self):
        """
        Allows the user to select a difficulty level by clicking on the corresponding text rectangle.
        The method continuously checks for mouse events and updates the selected_difficulty attribute accordingly.
        If the user closes the window, the method will exit the game.

        Returns:
            str: The selected difficulty level ('Easy' or 'Hard').
        """
        while self.selected_difficulty is None:
            for event in pygame.event.get(): # Check for events
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == MOUSEBUTTONDOWN: # Check for mouse click
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if self.text_easy_rect.collidepoint(mouse_x, mouse_y): # Check if the mouse click is on the 'Easy' text
                        self.selected_difficulty = 'Easy'
                    elif self.text_hard_rect.collidepoint(mouse_x, mouse_y): # Check if the mouse click is on the 'Hard' text
                        self.selected_difficulty = 'Hard'
        return self.selected_difficulty
    
    def difficulty_settings(self):
        """
        Sets the difficulty settings for the game.

        The difficulty settings include the speed of enemies, the rate at which enemies spawn,
        the speed of the player, and the speed of bullets.

        Returns:
            dict: A dictionary containing the difficulty settings.
        """
        EASY = { # Set the default values for easy difficulty   
            'enemy_speed': 8,
            'enemy_spawn_rate': 0.05,
            'player_speed': 5,
            'bullet_speed': 10
        }

        HARD = { # Increase the enemy speed, spawn rate, and player speed for hard difficulty
            'enemy_speed': 12,
            'enemy_spawn_rate': 0.4,
            'player_speed': 8,
            'bullet_speed': 12
        }

        return EASY if self.selected_difficulty == 'Easy' else HARD
