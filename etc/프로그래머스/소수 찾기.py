from math import sqrt
def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if func(i):
            answer += 1
    return answer

def func(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
print(solution(10))