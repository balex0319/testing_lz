import math

def log(f: float, g: float, h: float) -> float:
    if f <= 0:
        raise ValueError("f > 0")
    if h == 1:
        raise ValueError("h != 1")
    return math.log(f) + g / (h - 1)



    