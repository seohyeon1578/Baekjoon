# DFS + 완탐 + 백트레킹
# N x N 퀸 N
# 퀸의 범위 좌우 상하 대각선
# 한줄에 하나의 퀸이 들어갈 수 있다.
# 현재 노드의 위 좌우는 확인 X
# 대각선 만약 (0,0) 이면 (1,1) (2,2) 불가능 (1,0) 이면 (0,1) (2,1)
# 대각선인지 확인 공식 row - row = col - col
# 1. N을 입력받아 N만큼의 1차원 배열을 만든다 (2차원배열이 아닌 1차원배열인 이유: 한 row당 하나의 퀸이 들어갈 수 있기 때문에 인덱스를 깊이로 생각하고 값을 X로 지정하였다.)
# 2. DFS를 돌리는데 파라미터로 depth(깊이)가 주어진다.
# 3. 만약 깊이값이 입력받은 N의 값과 같다면 모든 깊이에 대한 찾기가 완료되었다.
# 4. graph의 n번째 행, i번째 열에 퀸을 넣어본다.
# 5. 만약 그 행에 둔 퀸이 같은열에 또 다른 퀸이 없으며 대각선상에도 다른 퀸이 없다면 True를 리턴하여 다음 행을 확인한다.(재귀)


N = int(input())
graph = [0] * N
count = 0

def promissing(n):
  for j in range(n):
    if graph[n] == graph[j] or abs(n - j) == abs(graph[n] - graph[j]):
      return False
  return True

def dfs(n):
  global count
  if n == N:
    count += 1
    return
  for i in range(N):
    graph[n] = i
    if promissing(n):
      dfs(n + 1)
dfs(0)
print(count)