# 토끼농장
# 나
# n = int(input())
# for i in range(n):
#     print('{}일:{}마리'.format(i + 1, i + (i+1)))
# 선생님
# def rabbit(n):
#     sum = 1
#     for i in range(1, n + 1):
#         print(f'{i}일:{sum}마리')
#         sum+=2
# rabbit(n)

# 눈덩이 만들기
# n, a, b = map(int, input().split())
# 나
# array = []
# for i in range(n):
#     array.append(a)
#     a *= b
# print(array)
# 선생님
# def snowball(n, a, b):
#   sequence = [a]
#   for i in range(1, n):
#      sequence.append(sequence[i - 1] * b)
#   return sequence
# result = snowball(n, a, b)
# print(result)

# 더 큰 숫자가 있나요?
# from itertools import permutations

# def str_permutations(s):
#     ps = permutations(s)
#     return list(map(int, sorted([''.join(p) for p in ps])))
# n, k = map(int, input().split())
# for i in str_permutations(str(n)):
#     if i > k:
#         print(i)
#         exit(0)
# print(-1)

# palindrome check
# s = input().replace(" ", "").lower()
# print(s == s[::-1])

# 두개의 문자열 공통 신호 찾기
# s1 = list(input())
# s2 = list(input())

# dp = [[0 for _ in range(len(s1) + 1)]for _ in range(len(s2) + 1)]
# Path = []
# for i in range(1, len(s1) + 1):
#     for j in range(1, len(s2) + 1):
#         if s1[i- 1] == s2[j - 1]:
#           dp[i][j] =  dp[i-1][j-1] + 1
#         else:
#            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# print(dp[len(s1)][len(s2)])

# def getText(r, o):
#   if i == 0 or o == 0:
#     return
#   if s1[r-1] == s2[o-1]:
#     Path.append(s1[r-1])
#     getText(r-1, o-1)
#   else:
#      if dp[r-1][o] > dp[r][o-1]:
#         getText(r-1, o)
#      else:
#         getText(r, o-1)
# getText(len(s1), len(s2))
# for i in Path[::-1]:
#    print(i, end="")

# 효율적인 피보나치 수열 구하기
# 1. 재귀함수만 사용한 풀이
# def fib(num):
#     if num < 2:
#         return num
#     return fib(num - 1) + fib(num - 2)
# num = int(input())
# print(fib(num))
# 2. 재귀함수 + DP 풀이
# top_down (재귀)
# def fib(num):
#     if dp[num] == -1:
#         dp[num] = fib(num - 1) + fib(num - 2)
#     return dp[num]
# num = int(input())
# dp = [-1] * 100
# dp[0] = 0
# dp[1] = 1
# print(fib(num))
# 3. DP 배열만 사용한 풀이 
# bottom_up (배열 순회) 제일 빠르다.
# num = int(input())
# dp = [0] * 100
# dp[1] = 1
# for i in range(2, num + 1):
#     dp[i] =dp[i-1] + dp[i - 2]
# print(dp[num])

# DFS, BFS로 탐색
# from collections import deque
# def dfs(idx):
#     global visited
#     visited[idx] = True
#     print(idx, end=" ")
#     for next in range(1, N + 1):
#         if not visited[next] and graph[idx][next]:
#             dfs(next)
# def bfs():
#     global visited
#     q = deque([V])
#     while q:
#         cur = q.popleft()
#         print(cur, end=" ")
#         for next in range(1, N + 1):
#             if not visited[next] and graph[cur][next]:
#                 visited[next] = True
#                 q.append(next)
# N, M, V = map(int, input().split())
# graph = [[False] * (N + 1) for _ in range(N + 1)]
# visited = [False] * (N + 1)

# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a][b] = True
#     graph[b][a] = True
# dfs(V)
# print()
# bfs() 

# from collections import deque
# def solution(Data, d, k):
#     queue = deque([1])
#     cnt = 0
#     while queue:
#         x = queue.popleft()
#         if x == len(Data) - 1:
#             break
#         if abs(Data[x] - Data[x + 1]) <= d:
#             cnt += 1
#             if cnt > k:
#                 break
#             del Data[x]
#             queue.append(x)
#         else:
#             print('2')
#             queue.append(x + 1)
#     return Data

# print(solution([1, 2, 3, 4, 5, 6, 7, 8], 1, 3))

from collections import deque
def solution(A, B, dis, dur):
    answer = ""
    queue = deque([A[0], B[0]])

    while queue:
        a, b = queue.popleft()
        time = 0
    return answer

print(solution([1, 7], [3, 8], 2, 2))