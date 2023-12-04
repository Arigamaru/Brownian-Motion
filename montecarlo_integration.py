import random
import numpy as np

def mcvol(n, r, d):
    count = 0
    for _ in range(n):
        point = [random.uniform(-r, r) for _ in range(d)]
        if sum([x**2 for x in point]) <= r**2:
            count += 1
    volume = (2 * r)**d * (count/n)
    return volume

n = int(1e6)
r = int(input("r = "))
d = int(input("d = "))
vol = mcvol(n,r,d) 
α = vol / (np.pi*r**d)  

print(f"Volume in {d} dimension: {vol}")
print(f"α for πr^{d}: {α:.6f}")
