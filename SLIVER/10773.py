K = int(input())
stack = []
answer = 0
for i in range(K):
    k = int(input())
    if k == 0 and stack:
        stack.pop()
    else:
        stack.append(k)

for i in stack:
    answer += i
print(answer)