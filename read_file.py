from funcion import *


#salva il file in una variabile
with open("map1.txt", "r", encoding="utf-8") as file:
    map1 = file.read()


#disegna la mappa
def draw_map(map):
	lines = map.splitlines()
	print (lines)
	for i in range(len(lines)):
		for ii in range(len(lines[i])):
			if lines[i][ii] == "X":
				draw_screen(ii, i, lines[i][ii], 34)
