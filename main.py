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
	squere1 = pygame.Rect(376,327 ,555,104)
	pygame.draw.rect(screen, (0, 0, 255), squere1)
	squere2 = pygame.Rect(191,329 ,184,104)
	pygame.draw.rect(screen, (0, 0, 255), squere2)
	squere3 = pygame.Rect(378,194 ,26,132)
	pygame.draw.rect(screen, (0, 0, 255), squere3)
	squere4 = pygame.Rect(404,193 ,108,34)
	pygame.draw.rect(screen, (0, 0, 255), squere4)
	squere5 = pygame.Rect(476,227 ,36,40)
	pygame.draw.rect(screen, (0, 0, 255), squere5)
	squere6 = pygame.Rect(512,237 ,120,30)
	pygame.draw.rect(screen, (0, 0, 255), squere6)
	squere7 = pygame.Rect(602,76 ,32,190)
	pygame.draw.rect(screen, (0, 0, 255), squere7)
	squere8 = pygame.Rect(10,-1 ,1280,28)
	pygame.draw.rect(screen, (0, 0, 255), squere8)
	squere9 = pygame.Rect(126,149 ,120,58)
	pygame.draw.rect(screen, (0, 0, 255), squere9)
	squere10 = pygame.Rect(2,23 ,124,184)
	pygame.draw.rect(screen, (0, 0, 255), squere10)
	squere11 = pygame.Rect(18,206 ,50,498)
	pygame.draw.rect(screen, (0, 0, 255), squere11)
	squere12 = pygame.Rect(54,678 ,390,46)
	pygame.draw.rect(screen, (0, 0, 255), squere12)
	squere13 = pygame.Rect(312,552 ,148,168)
	pygame.draw.rect(screen, (0, 0, 255), squere13)
	squere14 = pygame.Rect(460,552 ,0,0)
	pygame.draw.rect(screen, (0, 0, 255), squere14)
	squere15 = pygame.Rect(458,700 ,542,20)
	pygame.draw.rect(screen, (0, 0, 255), squere15)
	squere16 = pygame.Rect(512,76 ,98,34)
	pygame.draw.rect(screen, (0, 0, 255), squere16)
	squere17 = pygame.Rect(460,552 ,110,43)
	pygame.draw.rect(screen, (0, 0, 255), squere17)
	squere18 = pygame.Rect(644,552 ,446,40)
	pygame.draw.rect(screen, (0, 0, 255), squere18)
	squere19 = pygame.Rect(756,592 ,246,108)
	pygame.draw.rect(screen, (0, 0, 255), squere19)
	squere20 = pygame.Rect(1020,326 ,70,226)
	pygame.draw.rect(screen, (0, 0, 255), squere20)
	squere21 = pygame.Rect(994,590 ,96,31)
	pygame.draw.rect(screen, (0, 0, 255), squere21)
	squere22 = pygame.Rect(1000,704 ,284,12)
	pygame.draw.rect(screen, (0, 0, 255), squere22)
	squere23 = pygame.Rect(702,84 ,80,56)
	pygame.draw.rect(screen, (0, 0, 255), squere23)
	squere24 = pygame.Rect(702,140 ,36,128)
	pygame.draw.rect(screen, (0, 0, 255), squere24)
	squere25 = pygame.Rect(738,224 ,354,42)
	pygame.draw.rect(screen, (0, 0, 255), squere25)
	squere26 = pygame.Rect(1050,106 ,42,120)
	pygame.draw.rect(screen, (0, 0, 255), squere26)
	squere27 = pygame.Rect(1264,96 ,14,614)
	pygame.draw.rect(screen, (0, 0, 255), squere27)
	


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
