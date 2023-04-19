sequence = [1, 1, 1, 2, 3, 4, 5]
k = 5
sum = sequence[0]
left = 0
right = 0
answer = []
while True:
    if sum == k:
        answer.append([left, right])
    if left == len(sequence) and right == len(sequence):
        break
    if sum <= k and right < len(sequence):
        right += 1
        if right < len(sequence):
            sum += sequence[right]
    else:
        if left < len(sequence):
            sum -= sequence[left]
        left += 1
answer.sort(key=lambda x: (x[1] - x[0], x[0]))
print(answer[0])