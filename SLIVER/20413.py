N = int(input())
s, g, p, d = list(map(int, input().split()))
MVP = str(input())
arr = []
for i in list(MVP):
    x = 0
    if arr:
      x = arr[-1]
    if i == "B":
        arr.append(s-x-1)
    elif i == "S":
        arr.append(g-x-1)
    elif i == "G":
        arr.append(p-x-1)
    elif i == "P":
        arr.append(d-x-1)
    elif i == "D":
        arr.append(d)
print(sum(arr))
# 29 + 30 + 59 = 118
# 256 + 12 + 354 + 12 + 