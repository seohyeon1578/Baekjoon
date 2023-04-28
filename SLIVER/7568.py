N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
answer = []

for i in range(len(data)):
    cnt = 0
    for j in range(len(data)):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            cnt += 1
    answer.append(str(cnt + 1))      

print(' '.join(answer))