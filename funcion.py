import os
from bresenham_alg import bresenham_line

l0  = ['.']*128
l1  = ['.']*128
l2  = ['.']*128
l3  = ['.']*128
l4  = ['.']*128
l5  = ['.']*128
l6  = ['.']*128
l7  = ['.']*128
l8  = ['.']*128
l9  = ['.']*128
la  = ['.']*128
lb  = ['.']*128
lc  = ['.']*128
ld  = ['.']*128
le  = ['.']*128
lf  = ['.']*128
lg  = ['.']*128
lh  = ['.']*128
li  = ['.']*128
lj  = ['.']*128
lk  = ['.']*128
ll  = ['.']*128
lm  = ['.']*128
ln  = ['.']*128
lo  = ['.']*128
lp  = ['.']*128
lq  = ['.']*128
lr  = ['.']*128
ls  = ['.']*128
lt  = ['.']*128
lu  = ['.']*128
lv  = ['.']*128
lw  = ['.']*128
lx  = ['.']*128
ly  = ['.']*128
lz  = ['.']*128
l0a = ['.']*128
l1a = ['.']*128
l2a = ['.']*128
l3a = ['.']*128
l4a = ['.']*128
l5a = ['.']*128
l6a = ['.']*128
l7a = ['.']*128
l8a = ['.']*128
l9a = ['.']*128
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
	draw_screen(character["x"],character["y"],".","37")
	character["x"] = character["x"] + x
	character["y"] = character["y"] + y
	
	
	
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



