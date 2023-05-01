import sys;
from copy import deepcopy
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
stack = []
num = 99
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
direction = [
      [[0], [1], [2], [3]], # 1번 CCTV
      [[0, 1], [2, 3]], # 2번 CCTV
      [[0, 2], [0, 3], [1, 2], [1, 3]], # 3번 CCTV
      [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], # 4번 CCTV
      [[0, 1, 2, 3]] # 5번 CCTV
  ]
for i in range(N):
    for j in range(M):
        if arr[i][j] in [1, 2, 3, 4, 5]:
          stack.append([arr[i][j], j, i])  
def count_zero(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt
def dfs(depth,graph):
    global num
    if depth == len(stack):
        num = min(num, count_zero(graph))
        return
    new = deepcopy(arr)
    v, x, y = stack[depth]
    for dir in direction[v - 1]:
        watch(x, y, dir, new)
        dfs(depth + 1, new)
        new = deepcopy(arr)
def watch(x, y, dir, new):
    for d in dir:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]

            if 0 > nx or nx >= M or 0 > ny or ny >= N or new[ny][nx] == 6:
                break
            if new[ny][nx] != 0:
                continue
            new[ny][nx] == 7
dfs(0, arr)
print(num)