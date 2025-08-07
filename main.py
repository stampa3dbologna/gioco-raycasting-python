from funcion import *
from read_file import *
import msvcrt
from bresenham_alg import bresenham_line

player =  make_character (4,7,"a", "31" ,"player")
draw_character (player)

draw_map(map1)
draw_line(2,2,7,8,"a",31)
update_screen()


while True :

	if msvcrt.kbhit ():
		tasto = msvcrt.getch()
		if tasto == b'a': 
			move_character (-1,0,player, map1)
			draw_character (player)
			update_screen()
		if tasto == b'd': 
			move_character (1,0,player, map1)
			draw_character (player)
			update_screen()
		if tasto == b'w': 
			move_character (0,-1,player, map1)
			draw_character (player)
			update_screen()
		if tasto == b's': 
			move_character (0,1,player, map1)
			draw_character (player)
			update_screen()


