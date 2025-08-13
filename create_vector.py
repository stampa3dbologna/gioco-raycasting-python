import math

def point_in_direction(x0, y0, distance, angle_degrees):

    angle_radians = math.radians(angle_degrees)
    x = x0 + distance * math.cos(angle_radians)
    y = y0 + distance * math.sin(angle_radians)

    return (x, y)
	
