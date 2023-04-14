# 재귀함수
# 풀이 1.
# 1. 별을 9개의 공간으로 나누고, 좌상부터 1이라고 쳐 5번을 제외한 나머지 공간의 별에 똑같이 복사한다.
import sys
sys.setrecursionlimit(10 ** 6)# 재귀함수 시간초과 에러 방지

# def star(n):
#     if n == 3:
#         array[1] = ["*", " ", "*"]
#         array[0] = array[2] = ["*"]*3
#         print(array)
#         return
#     star(n//3)
#     for i in range(0, n, n//3):
#         for j in range(0, n, n//3):
#             if i != n//3 or j != n//3:
#                 for k in range(n//3):
#                     array[i+k][j:j + n//3] = array[k][:n//3]
# N = int(sys.stdin.readline())
# array = [[" "]*N for _ in range(N)]
# star(N)

# for i in range(N):
#     for j in range(N):
#         print(array[i][j], end="")
#     print()

# 풀이 2.
# 1. 공간을 1, 2, 3 즉 열 1, 열 2, 열 3으로 나눈 후 재귀함수를 통해 구해진 별을 붙인다.

def star(n):
    if n == 1:
        return ["*"]
    stars = star(n//3)
    array = []

    for s in stars:
        array.append(s*3)
    for s in stars:
        array.append(s + ' '*(n//3)+s)
    for s in stars:
        array.append(s*3)
    return array

N = int(sys.stdin.readline().strip())
print('\n'.join(star(N)))