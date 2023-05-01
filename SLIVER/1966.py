from collections import deque
K = int(input())
for i in range(K):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    temp = [0 for _ in range(N)]
    temp[M] = 1
    queue = deque(arr)
    cnt = 0

    while queue:
        if max(temp) == 0:
            break
        m = max(queue)
        x = queue.popleft()
        x_flag = temp[0]
        del temp[0]
        if x == m:
            cnt += 1
        else:
            queue.append(x)
            temp.append(x_flag)

    print(cnt)