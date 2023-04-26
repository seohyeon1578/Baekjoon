from collections import deque

priorities = [1, 1, 9, 1, 1, 1]
location = 0
answer = 0
array = [0 for _ in range(len(priorities))]
array[location] = 1
queue = deque(priorities)
while queue:
    if max(array) == 0:
        break
    max_queue = max(queue)
    target = queue.popleft()
    target_flag = array[0]
    del array[0]
    if target == max_queue:
        answer += 1
    else:
        queue.append(target)
        array.append(target_flag)
print(answer)