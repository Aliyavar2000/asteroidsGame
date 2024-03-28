import pygame

class Bullet:
    def __init__(self, position, velocity):
            """
            Initializes a new instance of the Bullet class.

            Args:
                position (tuple): The initial position of the bullet.
                velocity (tuple): The initial velocity of the bullet.

            Attributes:
                position (tuple): The current position of the bullet.
                velocity (tuple): The current velocity of the bullet.
                radius (int): The radius of the bullet.
                color (tuple): The color of the bullet.

            """
            self.position = position
            self.velocity = velocity
            self.radius = 3
            self.color = (255, 0, 0)

    def move(self):
        """
        Move the bullet by updating its position based on its velocity.

        This method updates the y-coordinate of the bullet's position by adding its velocity.

        Parameters:
        None

        Returns:
        None
        """
        self.position.y += self.velocity
       

    def draw(self, surface):
        """
        Draw the bullet on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the bullet on.
        """
        pygame.draw.circle(surface, self.color, (self.position.x, self.position.y), self.radius) # Draw the bullet as a circle
