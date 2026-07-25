import pygame

pygame.init()
screen = pygame.display.set_model((600,400))
game.display.set_caption("simple platformer")

clock = pygame.time.Clock()
player = pygame.React(50,300,40,60)
player_vel_y = 0
gravity = 1
jump_speed = -15
ground_y = 300
on_ground = True             
running = True
while running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	keys = pygame.key.get_pressed()

if keys[pygame.K.SPACE] and on_ground:
	 	player_vel_y += gravity
	 	player.y += player_vel_y
	 	if player.y >= ground_y:
	 		player.y = ground_y
	 		player_vel_y= 0
	 		on_ground = True

	 		screen.fill((135,206,232)) # sky blue 

py
