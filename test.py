def rotate90(list):
    n = len(list) #행 y
    m = len(list[0]) # 열 x
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n - i - 1] = list[i][j]
    return new
def rotate180(list):
    n = len(list) #행 y
    m = len(list[0]) # 열 x
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[m - j - 1][n - i - 1] = list[i][j]
    return new
def rotate270(list):
    n = len(list) #행 y
    m = len(list[0]) # 열 x
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[m - j - 1][i] = list[i][j]
    return new
print(rotate90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# 숫자 길이 100 = 3
from math import log10
print(int(log10(100)) + 1)

# 짝수
# if (n & 1) == 0
# 홀수
# if n & 1

# del array[idx]
# array.remove(value)

# 문자열 여러개
s = "absd/sdf asdf"
s = s.replace("/", " ")
s = s.split()

# 소수
from math import sqrt
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True   

# 진수 변환
def func(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return func(q, base) + T[r] if q else T[r]