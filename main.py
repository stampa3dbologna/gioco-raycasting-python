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
x = 611 
y = 647
direction = -90
x_hat, y_hat = point_in_direction(x, y, 15, direction)
player = pygame.Rect(x, y, 10, 10)
player_hat = pygame.Rect(x_hat, y_hat, 10, 10)
pygame.draw.rect(screen, (0, 255, 0), player)
pygame.draw.rect(screen, (127,255,0), player_hat)

map_img = pygame.image.load("tridente.png")
map_img.set_colorkey((0,0,0))
wall = pygame.Rect(0, 0, 10, 10)

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
    screen.fill((255,255,255))
    screen.blit(map_img,(0,0))    
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
    # fine quadrati mappa
    
    map_colision = [
        squere1,squere2,squere3,squere4,squere5,squere6,squere7,squere8,squere9,squere10,squere11,squere12,
        squere13,squere14,squere15,squere16,squere17,squere18,squere19,squere20,squere21,squere22,
        squere23,squere24,squere25,squere26,squere27
    ]
    
    for i in map_colision:
        pygame.draw.rect(screen,(0,0,255),i)
    
    if m_x != 0:
        direction = direction + (m_x / 4)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
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
    fov = 60  # campo visivo
    step = 1  # distanza tra i vari raggi
    max_distance = 500  # quanto diciamo, puo vedere il raggio
    points = [(x, y)]

    for angle_offset in range(-fov // 2, fov // 2 + 1, step):
        ray_angle = direction + angle_offset
        xr, yr = x, y
        distance = 0
        while not collide_map_point((xr, yr), map_colision) and distance < max_distance:
            xr, yr = point_in_direction(xr, yr, 5, ray_angle)
            distance += 5
        points.append((xr, yr))

    pygame.draw.polygon(screen, (255, 255, 150, 100), points)
    # Player
    x_hat,y_hat = point_in_direction(x,y,15,direction)
    player = pygame.Rect(x, y, 10, 10)
    player_hat = pygame.Rect(x_hat,y_hat,3,3)
    pygame.draw.rect(screen, (0, 255, 0), player)    
    pygame.draw.rect(screen, (255,255,0), player_hat)

    pygame.display.flip()
    clock.tick(60)  

pygame.quit()
