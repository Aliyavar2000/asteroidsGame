import pygame
from polygon import Polygon, Point
import random

class Enemy:
    def __init__(self, polygon, speed, screen_width, screen_height):
        """
        Initializes an instance of the Enemy class.

        Args:
            polygon (list): The polygon representing the enemy's shape.
            speed (int): The speed at which the enemy moves.
            screen_width (int): The width of the screen.
            screen_height (int): The height of the screen.
        """
        self.polygon = polygon
        self.speed = speed
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rect = self.calculate_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height

    def calculate_rect(self):
        """
        Calculates and returns the bounding rectangle of the enemy object.

        Returns:
            pygame.Rect: The bounding rectangle of the enemy object.
        """
        points = self.polygon.getPoints()
        min_x = min(p.x for p in points)
        max_x = max(p.x for p in points)
        min_y = min(p.y for p in points)
        max_y = max(p.y for p in points)
        return pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)

    def move(self):
            """
            Move the enemy object vertically on the screen.

            This method updates the position of the enemy object by moving it downwards
            with a speed defined by the `speed` attribute. If the enemy object goes
            beyond the screen height, it will be repositioned at a random x-coordinate
            at the top of the screen.

            Parameters:
                None

            Returns:
                None
            """
            self.polygon.move(0, self.speed)
            if self.polygon.getPosition().y > self.screen_height:
                self.polygon.setPosition(Point(random.randint(40, self.screen_width - 40), 0))
                self.rect = self.calculate_rect()  # Update the rect after moving

    def draw(self, surface):
        """
        Draw the enemy on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the enemy on.
        """
        points = self.polygon.getPoints()
        pygame.draw.polygon(surface, self.color, [(p.x, p.y) for p in points])

    def contains(self, point):
        """
        Check if the point is contained within the polygon.

        Parameters:
        - point: A tuple representing the coordinates of the point.

        Returns:
        - True if the point is inside the polygon, False otherwise.
        """
        return self.polygon.contains(point)
