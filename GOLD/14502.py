# 1. 시간 초과
from collections import deque
from itertools import combinations
import sys

sys.setrecursionlimit(10 ** 6)

def bfs():
    queue = deque([])
    for comb in combinations(empty, 3):         
      for i in range(n):
          for j in range(m):
              temp[i][j] = graph[i][j]
      for x, y in comb:
          temp[x][y] = 1
      for i in range(n):
          for j in range(m):
              if temp[i][j] == 2:
                  queue.append((i, j))
      while queue:
          x, y = queue.popleft()
          for i in range(4):
              nx, ny = x + dx[i], y + dy[i]
              if 0 <= nx < n and 0 <= ny < m:
                  if temp[nx][ny] == 0:
                      temp[nx][ny] = 2
                      queue.append((nx, ny))
      global result
      cnt = 0
      for i in range(n):
          cnt += temp[i].count(0)
      result = max(result, cnt)

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * m for i in range(n)]
empty = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = 0
bfs()
print(result)