# 1차 시간초과
from itertools import permutations
def solution(numbers):
    answer = 0
    numbers = list(map(str, numbers))
    array = list(permutations(numbers, len(numbers)))
    for i in range(len(array)):
        if answer < int(''.join(array[i])):
            answer = int(''.join(array[i]))
    return str(answer)

# 2차
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x : x * 3, reverse=True)
    return "".join(numbers) if numbers[0] != "0" else "0"
