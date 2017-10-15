import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Rectangle():

    def __init__(self):
        self.x = random.randrange(0,700)
        self.y = random.randrange(0,500)
        self.height =random.randrange(20,70)
        self.width = random.randrange(20,70)
        self.change_x=random.randrange(-3,3)
        self.change_y=random.randrange(-3,3)
        self.color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    def draw(self):
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        color = self.color
        pygame.draw.rect(screen, color,(x,y,width,height) )
    def move(self):
        self.x -= self.change_x
        self.y -= self.change_y

class Ellipse (Rectangle):
    def draw(self):
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        color = self.color
        pygame.draw.ellipse(screen, color,(x,y,width,height) )

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
my_list =[]
for el in range(1000):
    my_object = Rectangle()
    my_list.append(my_object)

for el in range(1000):
    my_object = Ellipse()
    my_list.append(my_object)



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    for el in my_list:
        el.draw()
        el.move()

    pygame.display.flip()

        # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
