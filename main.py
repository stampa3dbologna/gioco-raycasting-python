from bresenham_alg import bresenham_line
import pygame 
from create_vector import point_in_direction
import random
import math
import numpy as np


pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

# Carica le texture dei muri
wall_texture = pygame.image.load("MUro.png")  # Crea un'immagine
wall_texture = pygame.transform.scale(wall_texture, (64, 64)) 

vel = 4
x = 611 
y = 647
direction = -90
x_hat, y_hat = point_in_direction(x, y, 15, direction)
player = pygame.Rect(x, y, 1, 1)
pygame.draw.rect(screen, (0, 255, 0), player)

mode3d = True

a_pressd = None 
s_pressd = None 
w_pressd = None 
d_pressd = None 

def collide_map(player, map):
	for i in map:
		if player.colliderect(i):
			return True
	return False 

def collide_map_point(point, map):
	for i in map:
		if i.collidepoint(point):
			return True
	return False 

while running:
	screen.fill((128,0,0))
	m_x , m_y = pygame.mouse.get_rel()
	
	# quadrati per mappa
	squere1 = pygame.Rect(376,327 ,555,104)
	squere2 = pygame.Rect(191,329 ,184,104)
	squere3 = pygame.Rect(378,194 ,26,132)
	squere4 = pygame.Rect(404,193 ,108,34)
	squere5 = pygame.Rect(476,227 ,36,40)
	squere6 = pygame.Rect(512,237 ,120,30)
	squere7 = pygame.Rect(602,76 ,32,190)
	squere8 = pygame.Rect(10,-1 ,1280,28)
	squere9 = pygame.Rect(126,149 ,120,58)
	squere10 = pygame.Rect(2,23 ,124,184)
	squere11 = pygame.Rect(18,206 ,50,498)
	squere12 = pygame.Rect(54,678 ,390,46)
	squere13 = pygame.Rect(312,552 ,148,168)
	squere14 = pygame.Rect(460,552 ,0,0)
	squere15 = pygame.Rect(458,700 ,542,20)
	squere16 = pygame.Rect(512,76 ,98,34)
	squere17 = pygame.Rect(460,552 ,110,43)
	squere18 = pygame.Rect(644,552 ,446,40)
	squere19 = pygame.Rect(756,592 ,246,108)
	squere20 = pygame.Rect(1020,326 ,70,226)
	squere21 = pygame.Rect(994,590 ,96,31)
	squere22 = pygame.Rect(1000,704 ,284,12)
	squere23 = pygame.Rect(702,84 ,80,56)
	squere24 = pygame.Rect(702,140 ,36,128)
	squere25 = pygame.Rect(738,224 ,354,42)
	squere26 = pygame.Rect(1050,106 ,42,120)
	squere27 = pygame.Rect(1264,96 ,14,614)
	
	map_colision = [
		squere1,squere2,squere3,squere4,squere5,squere6,squere7,squere8,squere9,squere10,squere11,squere12,
		squere13,squere14,squere15,squere16,squere17,squere18,squere19,squere20,squere21,squere22,
		squere23,squere24,squere25,squere26,squere27
	]
	
	if m_x != 0:
		direction = direction + (m_x / 2)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	for i in map_colision:
		if mode3d == False:
			pygame.draw.rect(screen,(0,0,255),i)
	if pygame.key.get_just_pressed()[pygame.K_a]: 
		a_pressd = True
	if pygame.key.get_just_released()[pygame.K_a]:
		a_pressd = False
	if a_pressd: 
		new_x,new_y = point_in_direction(x,y,vel,direction-90)
		new_player = pygame.Rect(new_x, new_y, 10, 10)
		if not collide_map(new_player,map_colision):
			x = new_x
			y = new_y

	if pygame.key.get_just_pressed()[pygame.K_s]: 
		s_pressd = True
	if pygame.key.get_just_released()[pygame.K_s]:
		s_pressd = False
	if s_pressd:
		new_x,new_y = point_in_direction(x,y,vel,direction-180)
		new_player = pygame.Rect(new_x, new_y, 10, 10)
		if not collide_map(new_player,map_colision):
			y = new_y
			x = new_x

	if pygame.key.get_just_pressed()[pygame.K_w]: 
		w_pressd = True
	if pygame.key.get_just_released()[pygame.K_w]:
		w_pressd = False
	if w_pressd:
		new_x,new_y = point_in_direction(x,y,vel,direction)
		new_player = pygame.Rect(new_x, new_y, 10, 10)
		if not collide_map(new_player,map_colision):
			y = new_y
			x = new_x

	if pygame.key.get_just_pressed()[pygame.K_d]: 
		d_pressd = True
	if pygame.key.get_just_released()[pygame.K_d]:
		d_pressd = False
	if d_pressd:
		new_x,new_y = point_in_direction(x,y,vel,direction-270)
		new_player = pygame.Rect(new_x, new_y, 10, 10)
		if not collide_map(new_player,map_colision):
			x = new_x
			y = new_y
	
	# raggi multipli
	fov = 80  # campo visivo
	definition = 3
	step = 0.25	 # distanza tra i vari raggi
	max_distance = 700  # quanto diciamo, puo vedere il raggio
	points = []
	lenght_ray = []  # lunghezza raggi

	for angle_offset in np.arange(-fov // 2, fov // 2 + 1, step):
		ray_angle = direction + angle_offset
		xr, yr = x, y
		distance = 0
		while not collide_map_point((xr, yr), map_colision) and distance < max_distance:
			xr, yr = point_in_direction(xr, yr, definition, ray_angle)
			distance += definition
		
		# Store both the final point and the ray length
		points.append((xr, yr))
		lenght_ray.append(max_distance - distance)
	if mode3d == False:
		for i in range(len(points)) :
			pygame.draw.line(screen,(255,100,0),(x , y) ,(int(points[i][0]),int(points[i][1])) , 2)
	player = pygame.Rect(x, y, 1, 1)

	
	
	#inzio del raycasting
	height = screen.get_height()
	width  = screen.get_width() 
	line_step_y = height / max_distance 
	line_step_x = width / len(points)
	color_step = 256 / 500		
		
	for i in range(len(lenght_ray)):
		leght_line = round(lenght_ray[i] * line_step_y)
		color = int(round(((lenght_ray[i] * color_step))))
		start_line = int(height / 2) - round(leght_line / 2)
		if color > 255:
			color = 255
		if color < 1 :
			color = 1

		# Calcola la posizione x sulla texture
		wall_x = points[i][0] % wall_texture.get_width()
		
		# Estrae una colonna della texture
		texture_slice = pygame.Surface((1, wall_texture.get_height()))
		texture_slice.blit(wall_texture, (0, 0), (wall_x, 0, 1, wall_texture.get_height()))
		
		# Scala la slice all'altezza del muro
		if leght_line > 0:
			scaled_slice = pygame.transform.scale(texture_slice, (round(line_step_x), leght_line))
			
			# Applica l'effetto della distanza (fog)
			scaled_slice.fill((color, color, color), special_flags=pygame.BLEND_MULT)
			  
			# Disegna la slice
			if mode3d == True :
				screen.blit(scaled_slice, (round((i + 1) * line_step_x), start_line))
		
	pygame.display.flip()
	clock.tick(60)


pygame.quit()
