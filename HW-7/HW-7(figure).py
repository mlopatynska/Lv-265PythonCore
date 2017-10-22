import pygame
import random

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Rectangle():
    def __init__(self):
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 500)
        self.height = random.randint(20, 70)
        self.width = random.randint(20, 70)
        self.change_x = random.randint(-3, 3)
        self.change_y = random.randint(-3, 3)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self):
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        color = self.color
        pygame.draw.rect(screen, color, (x, y, width, height))

    def move(self):
        self.x -= self.change_x
        self.y -= self.change_y

class Ellipse(Rectangle):
    def draw(self):
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        color = self.color
        pygame.draw.ellipse(screen, color, (x, y, width, height))

pygame.init()

# Set the width and height of the screen [width, height]
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("figure")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

my_list = []
for i in range(500):
    my_object = Rectangle()
    my_list.append(my_object)
    my_object = Ellipse()
    my_list.append(my_object)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    for i in my_list:
        i.draw()
        i.move()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
