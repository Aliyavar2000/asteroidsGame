import pygame
from pygame.locals import *
from polygon import Polygon, Point
from enemy import Enemy
from player import Player
from background import Background
from bullet import Bullet
from difficulty_menu import DifficultyMenu
import random

class AsteroidAvoidanceGame:
        def __init__(self):
            """
            Initializes the Game class.

            This method sets up the game window, initializes game variables, and loads game assets.

            Parameters:
                None

            Returns:
                None
            """
            pygame.init() # Initialize the Pygame module
            pygame.mixer.init() # Initialize the Pygame mixer module
            self.FPS = 30 # Frames per second
            self.framesPerSec = pygame.time.Clock()
            self.window = pygame.display.set_mode((500, 600))
            pygame.display.set_caption('Asteroid Avoidance')
            self.screen_width, self.screen_height = pygame.display.get_surface().get_size() # Get the screen width and height
            self.background = Background() # Create a background object
            self.player = None
            self.enemygroup = []
            self.score = 0
            self.best_score = 0
            self.white = (255, 255, 255)
            self.red = (255, 0, 0)
            self.black = (0, 0, 0)
            self.font = pygame.font.Font(None, 36)

            self.player_shape = [
                Point(0, -20),   # Top point
                Point(10, 10),   # Right bottom point
                Point(5, 0),     # Middle point
                Point(-5, 0),    # Middle point
                Point(-10, 10)   # Left bottom point
            ]

            self.enemy_shape = [
                Point(0, -25),   # Top point
                Point(15, -10),  # Right top point
                Point(20, 0),    # Right middle point
                Point(15, 10),   # Right bottom point
                Point(0, 25),    # Bottom point
                Point(-15, 10),  # Left bottom point
                Point(-20, 0),   # Left middle point
                Point(-15, -10)  # Left top point
            ]

        def start(self):
            """
            Starts the game loop and manages the game flow.

            This method is responsible for initializing the game state, including the score, game over flag,
            and difficulty level. It also handles the display of the difficulty menu, selection of the difficulty,
            and starting and stopping the background music. Finally, it calls the `run_game_loop` method to start
            the main game loop and displays the game over screen when the game is over.
            """
            while True:
                pygame.mixer.music.load('music/music-for-arcade.mp3')
                pygame.mixer.music.play(-1) # Play the background music. The -1 argument makes the music loop indefinitely.
                self.start_time = pygame.time.get_ticks()
                self.score = 0
                self.game_over = False
                self.difficulty_manager = DifficultyMenu(self.window, self.screen_width, self.screen_height) # Create a difficulty manager object
                self.difficulty_manager.display_menu() # Display the difficulty menu
                selected_difficulty = self.difficulty_manager.select_difficulty() # Select the difficulty level
                self.set_difficulty(selected_difficulty)
                pygame.mixer.music.stop()
                pygame.mixer.music.load('music/epic-battle-153400.mp3')
                pygame.mixer.music.play(-1)
                self.run_game_loop() # Run the game loop
                self.display_game_over() # Display the game over screen

        def set_difficulty(self, difficulty):
            """
            Set the game difficulty level.

            Args:
                difficulty (str): The difficulty level to set. Can be 'Easy' or 'Hard'.

            Returns:
                None
            """
            if difficulty == 'Easy':
                player_speed = 5
                self.enemy_speed = 6  # Set enemy_speed as an instance variable
                bullet_speed = 10
            elif difficulty == 'Hard':
                player_speed = 8
                self.enemy_speed = 8  # Set enemy_speed as an instance variable
                bullet_speed = 12
            self.player = Player(player_speed, bullet_speed, self.screen_width, self.screen_height) # Create a player object
            self.enemygroup = [] # Initialize the enemy group
            self.best_score = max(self.score, self.best_score)

        def run_game_loop(self):
            """
            Runs the game loop until the game is over.
            """
            while not self.game_over: # Main game loop
                self.handle_events()
                self.update_objects()
                self.check_collisions()
                self.draw_objects()
                current_time = pygame.time.get_ticks()
                if current_time - self.start_time > 60000:
                    for enemy in self.enemygroup: # Increase the speed of the enemies after 60 seconds
                        enemy.speed += 1
                self.start_time = current_time
                self.framesPerSec.tick(self.FPS)
                self.best_score = max(self.score, self.best_score) # Update the best score if the current score is higher

        def handle_events(self):
            """
            Handle events from the Pygame event queue.

            This method iterates over the events in the Pygame event queue and handles them accordingly.
            If a QUIT event is detected, the Pygame module is quit and the program exits.

            Args:
                None

            Returns:
                None
            """
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        def update_objects(self):
            """
            Updates the game objects.

            This method updates the background, player, bullets, and enemies in the game.

            Parameters:
            - None

            Returns:
            - None
            """
            self.background.update()
            self.player.update_position() # Update the player's position
            self.player.update_bullets(self.window) # Update the player's bullets
            self.create_enemies() # Create new enemies
            for enemy in self.enemygroup:
                enemy.move()

        def create_enemies(self):
            """
            Create new enemies and add them to the enemy group.

            This method checks the length of the enemy group and creates new enemies if the number of enemies is less than 5.
            Each new enemy is created with a random position within the screen boundaries and added to the enemy group.

            Parameters:
            - self: The Game object.

            Returns:
            - None
            """
            if len(self.enemygroup) < 5: 
                new_enemy_polygon = Polygon(self.enemy_shape, Point(random.randint(40, self.screen_width - 40), 0), 0)
                new_enemy = Enemy(new_enemy_polygon, self.enemy_speed, self.screen_width, self.screen_height)
                self.enemygroup.append(new_enemy)

        def check_collisions(self):
            """
            Check for collisions between bullets and enemies, as well as between enemies and the player.

            This method iterates over the bullets fired by the player and the enemies in the game.
            If a bullet intersects with an enemy, both the bullet and the enemy are removed from their respective groups.
            Additionally, the player's score is incremented.
            If an enemy intersects with the player, the game is marked as over.

            Parameters:
                None

            Returns:
                None
            """
            for bullet in self.player.bullets[:]: # Iterate over a copy of the bullets list
                for enemy in self.enemygroup[:]: # Iterate over a copy of the enemy group list
                    if enemy.polygon.contains(bullet.position):
                        self.enemygroup.remove(enemy) # Remove the enemy from the enemy group
                        if bullet in self.player.bullets:
                            self.player.bullets.remove(bullet) # Remove the bullet from the player's bullets
                        self.score += 1
            for enemy in self.enemygroup:
                if enemy.polygon.contains(self.player.polygon.getPosition()): # Check if an enemy intersects with the player
                    self.game_over = True
                    break

        def draw_objects(self):
            """
            Draws all the game objects on the screen.

            This method fills the window with a black color, renders the background,
            draws the player, draws each enemy in the enemy group, displays the score,
            and updates the display.

            Parameters:
            - None

            Returns:
            - None
            """
            self.window.fill(self.black)
            self.background.render(self.window) # Render the background
            self.player.draw(self.window)
            for enemy in self.enemygroup:
                enemy.draw(self.window)
            self.display_score()
            pygame.display.update()

        def display_score(self):
            """
            Displays the current score on the game window.
            """
            score_text = self.font.render("Score: " + str(self.score), True, self.white)
            self.window.blit(score_text, (10, 10))

        def display_game_over(self):
            """
            Displays the game over screen with the final score and best score.
            """
            game_over_text = self.font.render("GAME OVER", True, self.black)
            text_rect = game_over_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            score_text = self.font.render("Score: " + str(self.score), True, self.white)
            score_text_rect = score_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 50))
            best_score_text = self.font.render("Best Score: " + str(self.best_score), True, self.white)
            best_score_text_rect = best_score_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 100))
            self.window.fill(self.red)
            self.window.blit(game_over_text, text_rect)
            self.window.blit(score_text, score_text_rect)
            self.window.blit(best_score_text, best_score_text_rect)
            pygame.display.update()
            pygame.time.delay(2000) # Delay for 2 seconds before restarting the game

# if __name__ == "__main__":
#     game = AsteroidAvoidanceGame()
#     game.start()
