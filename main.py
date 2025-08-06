import os
import msvcrt
from funcion import *
from bresenham_alg import bresenham_line

try:
    size = os.get_terminal_size()
    LARGHEZZA = size.columns - 1
    ALTEZZA = size.lines - 2
except OSError:
    LARGHEZZA = 80
    ALTEZZA = 23

def crea_mappa():
    return [["." for _ in range(LARGHEZZA)] for _ in range(ALTEZZA)]

def disegna_schermo(mappa, player):
    buffer = [riga[:] for riga in mappa]

    rosso = "\033[31m"
    reset = "\033[0m"
    buffer[player["y"]][player["x"]] = f"{rosso}{player['texture']}{reset}"
    
    os.system("cls")
    for riga in buffer:
        print("".join(riga))


mappa = crea_mappa()
player = make_character(4, 7, "a", "31", "player")


for x, y in bresenham_line(2, 2, 10, 8):
    if 0 <= x < LARGHEZZA and 0 <= y < ALTEZZA:
        mappa[y][x] = "b"


disegna_schermo(mappa, player)


while True:
    if msvcrt.kbhit():
        tasto = msvcrt.getch()

        if tasto == b'a' and player["x"] > 0:
            move_character(-1, 0, player)

        elif tasto == b'd' and player["x"] < LARGHEZZA - 1:
            move_character(1, 0, player)

        elif tasto == b'w' and player["y"] > 0:
            move_character(0, -1, player)

        elif tasto == b's' and player["y"] < ALTEZZA - 1:
            move_character(0, 1, player)

        disegna_schermo(mappa, player)
