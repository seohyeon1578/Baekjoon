def solution(order):
    answer = 0
    stack = []
    idx = 1
    while idx < len(order) + 1:
        stack.append(idx)
        while stack and  stack[-1] == order[answer]:
            stack.pop()
            answer += 1
        idx += 1      
    return answer
print(solution([4, 3, 1, 2, 5]))