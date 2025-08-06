def make_character(x, y, texture, color, name="unknown"):
    return {
        "x": x,
        "y": y,
        "texture": texture,
        "color": color,
        "name": name
    }

def move_character(dx, dy, character):
    character["x"] += dx
    character["y"] += dy
