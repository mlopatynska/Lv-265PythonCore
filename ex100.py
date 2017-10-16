import pygame

pygame.init()

black = ( 0, 0, 0)
white = (255, 255, 255)
green = ( 0, 255, 0)
red = (255, 0, 0)

class Rectangle():
#    x=0
#    y=0
#    change_x=0
#    change_y=0
#    width=10
#    height=10
#    color=green
#    def move(self):
#    self.x += self.change_x
#    self.y += self.change_y
    def draw(self, screen):
    pygame.draw.rect(screen, self.color, [self.x, self.y], self.width, self.height)

size=[700,500]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("My first game")

done=False

clock=pygame.time.Clock()

my_object = Rectangle()
my_object.x = 0
my_object.y = 0
my_object.color = green
my_object.change_x = 2
my_object.change_y = 2

while done==False:
    my_object.draw(screen)
    my_object.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    clock.tick(20)

pygame.quit()
