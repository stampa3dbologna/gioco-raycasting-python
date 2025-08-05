from funcion import *
import msvcrt


player =  make_character (4,7,"a","player")
draw_character (player)
update_screen()


while True :

	if msvcrt.kbhit():         
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
