from collections import deque
def solution(board):
    X, Y = len(board[0]), len(board)
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] 
    visited = [[-1] * X for _ in range(Y)]
    queue = deque([])

    for i in range(Y):
        for j in range(X):
            if board[i][j] == "R":
                queue.append([j, i, 0])
                visited[i][j] = 0
    
    while queue:
        x, y, cnt = queue.popleft()
        if board[y][x] == "G":
            return cnt
        for i in range(4):
            nx, ny = x, y
            while 0 <= nx + dx[i] < X and 0 <= ny + dy[i] < Y and board[ny + dy[i]][nx + dx[i]] != "D":
                nx += dx[i]
                ny += dy[i]
            if visited[ny][nx] > cnt + 1 or visited[ny][nx] == -1:
                visited[ny][nx] = cnt + 1
                queue.append([nx, ny, cnt + 1])
    return -1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))