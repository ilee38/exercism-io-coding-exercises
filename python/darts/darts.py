import math

def score(x, y):
    radius = math.sqrt(math.pow(x,2) + math.pow(y,2))
    #another opotion: radius = (x**2 + y**2)**0.5
    if radius > 10:
        return 0
    elif radius > 5 and radius <= 10:
        return 1
    elif radius > 1 and radius <= 5:
        return 5
    elif radius <= 1:
        return 10
