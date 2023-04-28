from math import sqrt
stack = []
def solution(numbers):
    answer = 0
    global stack
    func("", numbers)
    stack = set(stack)
    for i in stack:
        if isPrime(i):
            answer += 1
    return answer

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True        

def func(comb, numbers):
    global stack
    if len(comb) > 0:
        stack.append(int(comb))
    for i in range(len(numbers)):
        func(comb + numbers[i], numbers[0:i] + numbers[i+1:])
