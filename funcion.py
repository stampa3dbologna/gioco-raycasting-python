import os

l0 = ['.']*32
l1 = ['.']*32
l2 = ['.']*32
l3 = ['.']*32
l4 = ['.']*32
l5 = ['.']*32
l6 = ['.']*32
l7 = ['.']*32
l8 = ['.']*32
l9 = ['.']*32
la = ['.']*32
lb = ['.']*32
lc = ['.']*32
ld = ['.']*32
le = ['.']*32
lf = ['.']*32

r = [l0 , l1 ,l2,l3,l4,l5,l6,l7,l8,l9,la,lb,lc,ld,le,lf]

def draw_screen (x,y,texture):
	r[y][x] = texture
	
def move_character (x,y,character):
	character["x"] = character["x"] + x
	character["y"] = character["y"] + y
	
	
	
def make_character (x,y,texture,name):
	stats_charcter = {
	"x":x,
	"y":y,
	"texture":texture,
	"name":name
	}
	return stats_charcter
	
def draw_character (character):
	draw_screen (character["x"],character["y"],character["texture"])
	

def update_screen():
	os.system('cls')
	for i in r:
		printing_line = ""
		for ii in i:
			printing_line += ii
		print(printing_line)

