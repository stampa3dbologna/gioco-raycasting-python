from funcion import *
from read_file import *
import msvcrt
from bresenham_alg import bresenham_line
import pygame 

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True


vel = 2
x = 300
y = 350
player = pygame.Rect(x, y, 10, 10)
pygame.draw.rect(screen, (0, 255, 0), player)

map_img = pygame.image.load("Mappa.PNG")
map_img.set_colorkey((0,0,0))
wall = map_img

a_pressd = None 
s_pressd = None 
w_pressd = None 
d_pressd = None 

while running:

	screen.fill((0,0,0))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	if pygame.key.get_just_pressed()[pygame.K_a]: 
		a_pressd = True
	
	if pygame.key.get_just_released()[pygame.K_a]:
		a_pressd = False
	
	if a_pressd :
		new_x = x - vel
		new_player = pygame.Rect(new_x, y, 10, 10)
		if not new_player.colliderect(wall):
			x = new_x

	if pygame.key.get_just_pressed()[pygame.K_s]: 
		s_pressd = True
	
	if pygame.key.get_just_released()[pygame.K_s]:
		s_pressd = False
	
	if s_pressd:
		new_y = y + vel
		new_player = pygame.Rect(x, new_y, 10, 10)
		if not new_player.colliderect(wall):
			y = new_y

	if pygame.key.get_just_pressed()[pygame.K_w]: 
		w_pressd = True
	
	if pygame.key.get_just_released()[pygame.K_w]:
		w_pressd = False
	
	if w_pressd:
		new_y = y - vel
		new_player = pygame.Rect(x, new_y, 10, 10)
		if not new_player.colliderect(wall):
			y = new_y

	if pygame.key.get_just_pressed()[pygame.K_d]: 
		d_pressd = True
	
	if pygame.key.get_just_released()[pygame.K_d]:
		d_pressd = False
	
	if d_pressd:
		new_x = x + vel
		new_player = pygame.Rect(new_x, y, 10, 10)
		if not new_player.colliderect(wall):
			x = new_x
			
	screen.blit(wall,(0,0))	
	player = pygame.Rect(x, y, 10, 10)
	pygame.draw.rect(screen, (0, 255, 0), player)	

	
	pygame.display.flip()
	clock.tick(60)  

pygame.quit()

'''

player =  make_character (4,7,"a", "31" ,"player")
draw_character (player)

draw_map(map1)


while True :

	if msvcrt.kbhit ():
		tasto = msvcrt.getch()
		if tasto == b'a': 
			move_character (-1,0,player)
			draw_character (player)
			update_screen()
		if tasto == b'd': 
			move_character (1,0,player)
			draw_character (player)
			update_screen()
		if tasto == b'w': 
			move_character (0,-1,player)
			draw_character (player)
			update_screen()
		if tasto == b's': 
			move_character (0,1,player)
			draw_character (player)
			update_screen()

'''
