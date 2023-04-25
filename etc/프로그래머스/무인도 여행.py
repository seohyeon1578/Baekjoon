from collections import deque
def solution(maps):
    answer = []
    Y, X = len(maps), len(maps[0])
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    visited = [[False] * X for _ in range(Y)]
    queue = deque([])

    for i in range(Y):
        for j in range(X):
            if maps[i][j] != "X" and not visited[i][j]:
                sum = 0
                queue.append([i, j])

                while queue:
                    y, x = queue.popleft()
                    if visited[y][x]:
                        continue
                    
                    visited[y][x] = True
                    sum += int(maps[y][x])

                    for k in range(4):
                      nx, ny = dx[k] + x, dy[k] + y
                      if 0 <= nx < X and 0 <= ny < Y and maps[ny][nx] != "X" and not visited[ny][nx]:
                          queue.append([ny, nx])
                
                answer.append(sum)
    return sorted(answer) if answer else [-1] 

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))