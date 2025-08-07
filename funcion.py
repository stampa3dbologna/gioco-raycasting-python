import os
from bresenham_alg import bresenham_line
width = 100

l0  = ['.']*width
l1  = ['.']*width
l2  = ['.']*width
l3  = ['.']*width
l4  = ['.']*width
l5  = ['.']*width
l6  = ['.']*width
l7  = ['.']*width
l8  = ['.']*width
l9  = ['.']*width
la  = ['.']*width
lb  = ['.']*width
lc  = ['.']*width
ld  = ['.']*width
le  = ['.']*width
lf  = ['.']*width
lg  = ['.']*width
lh  = ['.']*width
li  = ['.']*width
lj  = ['.']*width
lk  = ['.']*width
ll  = ['.']*width
lm  = ['.']*width
ln  = ['.']*width
lo  = ['.']*width
lp  = ['.']*width
lq  = ['.']*width
lr  = ['.']*width
ls  = ['.']*width
lt  = ['.']*width
lu  = ['.']*width
lv  = ['.']*width
lw  = ['.']*width
lx  = ['.']*width
ly  = ['.']*width
lz  = ['.']*width
l0a = ['.']*width
l1a = ['.']*width
l2a = ['.']*width
l3a = ['.']*width
l4a = ['.']*width
l5a = ['.']*width
l6a = ['.']*width
l7a = ['.']*width
l8a = ['.']*width
l9a = ['.']*width
r = [
    l0 , l1 , l2 , l3 , l4 , l5 , l6 , l7 , l8 , l9 ,
    la , lb , lc , ld , le , lf , lg , lh , li , lj ,
    lk , ll , lm , ln , lo , lp , lq , lr , ls , lt ,
    lu , lv , lw , lx , ly , lz , l0a, l1a, l2a, l3a,
    l4a, l5a, l6a, l7a, l8a, l9a
]
def draw_screen (x,y,texture,color):
	r[y][x] = "\33[" + str(color) + "m" + texture + "\033[0m"
	
def move_character (x,y,character):
	draw_screen(character["x"],character["y"], "." ,"37")
	character["x"] = character["x"] + x
	character["y"] = character["y"] + y
	
	if is_free(new_x, new_y, map_text):
            draw_screen(character["x"], character["y"], ".", "37") 
            character["x"] = new_x
            character["y"] = new_y

def draw_map(map_text):
    lines = map_text.splitlines()
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "X":
                draw_screen(x, y, "X", 34)  
            else:
                draw_screen(x, y, ".", 37) 
		
	
def make_character (x,y,texture,color,name):
	stats_charcter = {
	"x":x,
	"y":y,
	"texture":texture,
	"color":color,
	"name":name
	}
	return stats_charcter
	
def draw_character (character):
	draw_screen (character["x"],character["y"],character["texture"],character["color"])
	
def draw_line (x1,y1,x2,y2,texture,color):
	line = bresenham_line(x1,y1,x2,y2)
	for i in line :
		draw_screen(i[0],i[1], texture , color)

def update_screen():
	os.system('cls')
	for i in r:
		printing_line = ""
		for ii in i:
			printing_line += ii
		print(printing_line)

def is_free(x, y, map_text):
    lines = map_text.splitlines()
    if y < 0 or y >= len(lines):
        return False
    if x < 0 or x >= len(lines[y]):
        return False
    return lines[y][x] != 'X'
