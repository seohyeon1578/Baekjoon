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
for i in answer:
    if i == answer[-1]:
        print(f'{i}', end="")
    else:
        print(f'{i}, ', end="")
print(">", end="")