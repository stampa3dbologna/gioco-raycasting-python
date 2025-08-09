from funcion import *
from read_file import *
import msvcrt
from bresenham_alg import bresenham_line
import pygame 
from create_vector import point_in_direction

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True


vel = 2
x = 300
y = 350
direction = -90
x_hat,y_hat = point_in_direction(x,y,15,direction)
player = pygame.Rect(x, y, 10, 10)
player_hat = pygame.Rect(x_hat,y_hat ,10,10)
pygame.draw.rect(screen, (0, 255, 0), player)
pygame.draw.rect(screen, (127,255,0), player_hat)

map_img = pygame.image.load("tridente.png")
map_img.set_colorkey((0,0,0))
wall = pygame.Rect(0, 0, 10, 10)

a_pressd = None 
s_pressd = None 
w_pressd = None 
d_pressd = None 

coord1 = 0,0

while running:

	
	screen.fill((255,255,255))
	screen.blit(map_img,(0,0))	
	m_x , m_y = pygame.mouse.get_rel()
	
	#quadrato per mappa
	squere1 = pygame.Rect(130,220 ,240,90)
	pygame.draw.rect(screen, (0, 0, 255), squere1)
	squere2 = pygame.Rect(284,492 ,136, 152)
	pygame.draw.rect(screen, (0, 0, 255), squere2)	
#	squere3 = pygame.Rect(420,584 ,179, 222)
#	pygame.draw.rect(screen, (0, 0, 255), squere3)	
	squere4 = pygame.Rect(564,490 ,830, 158)
	pygame.draw.rect(screen, (0, 0, 255), squere4) 
	squere5 = pygame.Rect(566,290 ,194, 40)
	pygame.draw.rect(screen, (0, 0, 255), squere5) 
	squere6 = pygame.Rect(768,112 ,180, 56)
	pygame.draw.rect(screen, (0, 0, 255), squere6) 


	#fine quadrati mappa
	
	
	if m_x != 0:
		direction = direction + (m_x / 4)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	if pygame.key.get_just_pressed()[pygame.K_a]: 
		a_pressd = True
	
	if pygame.key.get_just_released()[pygame.K_a]:
		a_pressd = False
	
	if a_pressd :
		new_x,new_y = point_in_direction(x,y,vel,direction-90)
		new_player = pygame.Rect(new_x, new_y, 10, 10)
		if not new_player.colliderect(wall):
			x = new_x
			y = new_y

	if pygame.key.get_just_pressed()[pygame.K_s]: 
		s_pressd = True
	
	if pygame.key.get_just_released()[pygame.K_s]:
		s_pressd = False
	
	if s_pressd:
		new_x,new_y = point_in_direction(x,y,vel,direction-180)
		new_player = pygame.Rect(new_x, new_y, 10, 10)
		if not new_player.colliderect(wall):
			y = new_y
			x = new_x

	if pygame.key.get_just_pressed()[pygame.K_w]: 
		w_pressd = True
	
	if pygame.key.get_just_released()[pygame.K_w]:
		w_pressd = False
	
	if w_pressd:
		new_x,new_y = point_in_direction(x,y,vel,direction)
		new_player = pygame.Rect(new_x, new_y, 10, 10)
		if not new_player.colliderect(wall):
			y = new_y
			x = new_x

	if pygame.key.get_just_pressed()[pygame.K_d]: 
		d_pressd = True
	
	if pygame.key.get_just_released()[pygame.K_d]:
		d_pressd = False
	
	if d_pressd:
		new_x,new_y = point_in_direction(x,y,vel,direction-270)
		new_player = pygame.Rect(new_x, new_y, 10, 10)
		if not new_player.colliderect(wall):
			x = new_x
			y = new_y
	

	if pygame.key.get_just_pressed()[pygame.K_p]: 
		coord1 = x , y
		print (x,y)
	if pygame.key.get_just_pressed()[pygame.K_l]: 
		print (x - coord1[0] , y - coord1[1])

	x_hat,y_hat = point_in_direction(x,y,15,direction)
	player = pygame.Rect(x, y, 10, 10)
	player_hat = pygame.Rect(x_hat,y_hat,10,10)
	pygame.draw.rect(screen, (0, 255, 0), player)	
	pygame.draw.rect(screen, (255,255,0), player_hat)

	
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


