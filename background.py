import pygame

class Background:
    def __init__(self):
        """
        Initializes the Background object.

        Loads the background image, sets the initial position and movement speed.

        Parameters:
        None

        Returns:
        None
        """
        self.image = pygame.image.load('pics/background.jpeg') # Load the background image
        self.rect_bg = self.image.get_rect() # Get the rect of the background image
        self.bg_Y = 0
        self.bg_x = 0
        self.bg_Y2 = -self.rect_bg.height
        self.bg_x2 = 0
        self.move_speed = 5

    def update(self):
        """
        Update the background position.

        This method updates the position of the background image based on the move speed.
        It also handles wrapping the background image when it goes off the screen.

        """
        self.bg_Y += self.move_speed
        self.bg_Y2 += self.move_speed
        if self.bg_Y > self.rect_bg.height: # If the first image goes off the screen, reset its position
            self.bg_Y = -self.rect_bg.height
        if self.bg_Y2 > self.rect_bg.height: # If the second image goes off the screen, reset its position
            self.bg_Y2 = -self.rect_bg.height

    def render(self, surface):
        """
        Renders the background on the given surface.

        Args:
            surface (pygame.Surface): The surface to render the background on.
        """
        surface.blit(self.image, (self.bg_x, self.bg_Y))
        surface.blit(self.image, (self.bg_x2, self.bg_Y2))
