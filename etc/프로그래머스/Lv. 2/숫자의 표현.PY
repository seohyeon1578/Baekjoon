# 1차 성공했지만 효율성이 떨어져보임 6.03ms
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        sum = 0
        for j in range(i, n + 1):
            sum += j
            if sum == n:
                answer += 1
            if sum > n:
                break
    return answer
# 2차 4.32ms 1초정도 줄었다.
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        sum = 0
        while sum < n:
            sum += i
            i += 1
            if sum == n:
                answer += 1
                break
    return answer

# 3차 0.23ms 아주 효율적으로 줄었다.
def solution(n):
    answer = 0
    for i in range(1, n + 1, 2):
        if n % i == 0:
            answer += 1
    return answer