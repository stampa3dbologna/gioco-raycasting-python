from funcion import *
import msvcrt
from bresenham_alg import bresenham_line

player =  make_character (4,7,"a", "31" ,"player")
draw_character (player)
update_screen()
print (bresenham_line(2,2,7,8))
draw_line(2,2,7,8,"a",31)


while True :

	if msvcrt.kbhit ():        #lll 
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
