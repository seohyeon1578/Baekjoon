from math import sqrt, floor, ceil
r1, r2 = 2, 3
answer = 0
for i in range(1, r2 + 1):
    y1 = ceil(sqrt(r1 ** 2 - i ** 2)) if r1 > i else 0
    y2 = floor(sqrt(r2 ** 2 - i ** 2))
    answer += y2 - y1 + 1    
answer *= 4
print(answer) 