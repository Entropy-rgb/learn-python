#A Pythagorean triplet is a set of three natural numbers, a > b > c, for which, 
#a^2 + b^2 = c^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000
from math import sqrt

for a in range(1,1000):
    for b in range(1, 1000 - a):
        c = sqrt((a**2) + (b**2))
        d = 1000 - a - b
        if d == c :
            print(f"a is {a} and b is {b} and c is {c} and abc is {a*b*c}")
        else:
            pass
