import pygame, sys
import time
import random

pygame.init()

screen_width=900
screen_height=800

black=(0,0,0)
white=(255,255,255)
red=(150,0,0)
green=(0,150,0)
blue=(0,0,255)
light_red=(255,0,0)
light_green=(0,255,0)

pause=False

gameScreen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("My First Game")
clock=pygame.time.Clock()

car_image=pygame.image.load("police_car.png")

def blocks_passed(count):
	font=pygame.font.SysFont("Comic Sans MS",30)
	text=font.render("Passed: "+str(count), True, green)
	gameScreen.blit(text,(0,0))

def blocks(blockx,blocky,blockw,blockh,color):
	pygame.draw.rect(gameScreen,color,[blockx,blocky,blockw,blockh])

def car(x,y):
	gameScreen.blit(car_image,(x,y))

def text_objects(text,font,color):
	textSurface=font.render(text, True, color)
	return textSurface,textSurface.get_rect()

def message_display(text):
	largeText=pygame.font.SysFont("Comic Sans MS",120)
	TextSurf,TextRect =text_objects(text,largeText,red)
	TextRect.center=((screen_width/2),(screen_height/2))
	gameScreen.blit(TextSurf,TextRect)
	pygame.display.update();
	time.sleep(1)
	game_loop()

def button(text,color,acolor,x,y,w,h,action=None):
	mouse=pygame.mouse.get_pos()
	click=pygame.mouse.get_pressed()
	if mouse[0]<x+w and mouse[0]>x and mouse[1]<y+h and mouse[1]>y:
		pygame.draw.rect(gameScreen,acolor,(x,y,w,h))
		if click[0]==1 and action != None:
			action()
	else:
		pygame.draw.rect(gameScreen,color,(x,y,w,h))
	smallText=pygame.font.SysFont("Comic Sans MS",25)
	TextSurf,TextRect=text_objects(text,smallText,black)
	TextRect.center=((x+w/2),(y+h/2))
	gameScreen.blit(TextSurf,TextRect)
        
def crash():
	largeText=pygame.font.SysFont("Comic Sans MS",70)
	TextSurf,TextRect =text_objects("CRASH!!!",largeText,blue)
	TextRect.center=((screen_width/2),(screen_height/2))
	gameScreen.blit(TextSurf,TextRect)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		button("PLAY AGAIN!",red,light_red,200,450,160,50,game_loop)
		button("QUIT",green,light_green,500,450,100,50,quit)

		pygame.display.update()
		clock.tick(70)

def game_intro():
	intro=True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			gameScreen.fill(white)
			largeText=pygame.font.SysFont("Comic Sans MS",100)
			TextSurf,TextRect =text_objects("CAR RACE",largeText,black)
			TextRect.center=((screen_width/2),(screen_height/2))
			gameScreen.blit(TextSurf,TextRect)
			button("PLAY",red,light_red,200,450,100,50,game_loop)
			button("QUIT",green,light_green,500,450,100,50,quit)

			pygame.display.update()
			clock.tick(70)

def unpause():
	global pause
	pause=False

def paused():
	global pause
	pause=True
	largeText=pygame.font.SysFont("Comic Sans MS",70)
	TextSurf,TextRect =text_objects("PAUSED",largeText,black)
	TextRect.center=((screen_width/2),(screen_height/2))
	gameScreen.blit(TextSurf,TextRect)
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		button("CONTINUE",red,light_red,200,450,160,50,unpause)
		button("QUIT",green,light_green,500,450,100,50,quit)

		pygame.display.update()
		clock.tick(70)


def game_loop():
		x=(screen_width * 0.50)
		y=(screen_height * 0.5)
		i=0
		car_width=140
		x_change=0
		passed=0

		block_width=100
		block_startx=random.randrange(0,screen_width-block_width)
		block_starty=-600
		block_speed=4
		block_height=100

		crashed=False

		while not crashed:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				i+=0.02
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						x_change=-(8+i)
					if event.key == pygame.K_RIGHT:
						x_change=8+i
					if event.key == pygame.K_p:
						paused()
				if event.type ==pygame.KEYUP:
					if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
						x_change=0

			x+=x_change
			gameScreen.fill(white)
			blocks(block_startx,block_starty,block_width,block_height,black)
			block_starty+=block_speed
			car(x,y)
			blocks_passed(passed)

			if x > screen_width-car_width or x<0:
				crash()
			
			if block_starty > screen_height:
				block_starty=0-block_height
				block_startx=random.randrange(0,screen_width-block_width)
				passed+=1
				block_speed+=0.33

			if y<block_starty+block_height:
				#print("y crossover")
				if x>block_startx and x<block_startx+block_width or x+car_width>block_startx and x+car_width<block_startx+block_width or x<block_startx and x+car_width>block_startx+block_width: 
					#print("x crossover")
					crash()

			pygame.display.update()
			clock.tick(70)

game_intro()
game_loop()
pygame.quit()