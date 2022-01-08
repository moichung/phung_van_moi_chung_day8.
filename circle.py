import numpy as np
from sys import argv

def circleArea(r):
    return np.pi * r**2

r = float(argv[1])

print(f"Diện tích hình tròn bán kính {r} là {circleArea(5)}")
