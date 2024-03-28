# player.py

import pygame
from polygon import Polygon, Point
from bullet import Bullet

class Player:
    def __init__(self, speed, bullet_speed, screen_width, screen_height):
        """
        Initializes the Player object.

        Parameters:
        - speed (int): The speed of the player's spaceship.
        - bullet_speed (int): The speed of the bullets fired by the player's spaceship.
        - screen_width (int): The width of the game screen.
        - screen_height (int): The height of the game screen.
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.polygon_shape = [ # Polygon shape of the player's spaceship
            Point(0, -20),   # Top point
            Point(10, 10),   # Right bottom point
            Point(5, 0),     # Middle point
            Point(-5, 0),    # Middle point
            Point(-10, 10)   # Left bottom point
        ]
        self.color = (255, 255, 255)  # White color for the player's spaceship
        self.speed = speed
        self.bullet_speed = bullet_speed
        self.polygon = Polygon(self.polygon_shape, Point(self.screen_width // 2, self.screen_height - 70), 0)  # Initial position centered at the bottom
        self.bullets = []

    def update_position(self):
        """
        Updates the position of the player based on the user input.

        The player's position is updated based on the keys pressed by the user.
        If the left arrow key is pressed and the player's x-coordinate is greater than 0,
        the player moves to the left by the specified speed.
        If the right arrow key is pressed and the player's x-coordinate is less than the screen width,
        the player moves to the right by the specified speed.
        If the spacebar key is pressed, the player shoots.

        Parameters:
        - None

        Returns:
        - None
        """
        pressed_keys = pygame.key.get_pressed() # Get the keys pressed by the user
        if self.polygon.getPosition().x > 0 and pressed_keys[pygame.K_LEFT]: # Check if the player is within the screen boundaries and the left arrow key is pressed
            self.polygon.move(-self.speed, 0)
        if self.polygon.getPosition().x < self.screen_width and pressed_keys[pygame.K_RIGHT]: # Check if the player is within the screen boundaries  and the right arrow key is pressed
            self.polygon.move(self.speed, 0)

        if pressed_keys[pygame.K_SPACE]: # Check if the spacebar key is pressed and shoot a bullet
            self.shoot()

    def draw(self, surface):
        """
        Draw the player on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the player on.
        """
        points = self.polygon.getPoints() # Get the points of the player's spaceship
        pygame.draw.polygon(surface, self.color, [(p.x, p.y) for p in points]) # Draw the player's spaceship
        for bullet in self.bullets:
            bullet.draw(surface) # Draw the bullets

    def shoot(self):
        """
        Shoots a bullet from the player's position with a specific velocity.

        Returns:
            None
        """
        bullet_position = Point(self.polygon.getPosition().x, self.polygon.getPosition().y) # Shoot from the player's position
        bullet_velocity = -self.bullet_speed  # Use the bullet_speed defined based on difficulty
        bullet = Bullet(bullet_position, bullet_velocity)
        self.bullets.append(bullet) # Add the bullet to the list of bullets

    def update_bullets(self, surface):
        """
        Update the position of bullets and remove any bullets that have gone off the screen.

        Args:
            surface: The surface on which the bullets will be drawn.

        Returns:
            None
        """
        for bullet in self.bullets: # Update the position of each bullet
            bullet.move()
            if bullet.position.y < 0:
                self.bullets.remove(bullet)
            bullet.draw(surface)
