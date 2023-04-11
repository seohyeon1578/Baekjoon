# 보관 후 하루가 지나면 왼쪽, 오른쪽, 앞, 뒤 토마토가 익는다.
# 1 = 익음, 0 = 익지 않, -1 = 없
# BFS 활용 문제
# 1. 이미익은(1) 토마토를 찾아서 위치를 큐에 담는다
# 2. BFS 탐색을 통해 다음 방문할 노드를 꺼내서 현재 노드의 상 우 하 좌를 모두 체크한다.
# 3. 노드가 상자의 범위를 벗어나지 않으며 덜 익은 토마토라면 해당 노드에 날짜를 표시한다. (날짜는 1부터 시작 하루가 지나면 2이다)
# 4. 그 후 큐에 추가하고 2-3을 반복한다.
# 5. BFS탐색을 끝낸 후 상자를 탐색하여 덜 익은 토마토가 있는지 확인하다.
# 6. 덜 익은 토마토가 있다면 -1을 출력하고, 모든 토마토가 다 익었다면 걸린 최대 일수를 계산한다. (최대 일수는 1부터시작하기에 -1을 해 주어야하며 상자에서 가장 높은 숫자를 찾으면 된다.)

from collections import deque
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])
dcnt = 0
# 상 우 하 좌
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i, j])
while queue:
    nodeN, nodeM = queue.popleft()
    for i in range(4):
        nx, ny = dx[i] + nodeM, dy[i] + nodeN
        if 0 <= nx < M and 0 <= ny < N:
            if box[ny][nx] == 0:
                box[ny][nx] = box[nodeN][nodeM] + 1
                queue.append([ny, nx])
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit()
        if dcnt < box[i][j]:
            dcnt = box[i][j]
print(dcnt - 1)