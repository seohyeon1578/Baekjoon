from itertools import combinations

def solution(numbers):
    answer = []
    array = list(combinations(numbers, 2))
    for i in range(len(array)):
        n, n2 = array[i]
        answer.append(n + n2)
    return sorted(list(set(answer)))            

print(solution([2,1,3,4,1]))