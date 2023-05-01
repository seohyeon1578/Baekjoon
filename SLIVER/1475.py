from math import ceil
N = list(input())
count = [N.count(str(i)) for i in range(0, 10)]
count[6] = ceil((count[6] + count[9]) / 2)

max = 0
for i in range(0, 9):
    if max < count[i]:
        max = count[i]
print(max)