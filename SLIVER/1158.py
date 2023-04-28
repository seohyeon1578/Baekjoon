from collections import deque
N, K = map(int, input().split())
queue = deque([i for i in range(1, N + 1)])
answer = []
while queue:
    for i in range(K):
        x = queue.popleft()
        if i == K - 1:
          answer.append(x)
        else:  
          queue.append(x)

print("<", end="")
for i in range(N):
    if (i != N -1):
        print(f'{answer[i]}, ', end="")
    else:
        print(f'{answer[i]}', end="")
print('>', end="")

# 1 2 3 4 5 6 7
# 3
# 4 5 6 7 1 2
# 3 6
# 7 1 2 4 5
# 3 6 2
# 4 5 7 1
# 3 6 2 7
# 1 4 5
# 3 6 2 7 5
# 1 4
