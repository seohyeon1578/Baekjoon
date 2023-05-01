temp = [[0] * 101 for _ in range(101)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            temp[x + i][y + j] = 1
answer = 0
for i in temp:
    answer += sum(i)
print(answer)