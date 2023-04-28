def d(n):
    arr = list(str(n))
    answer = n
    for i, v in enumerate(arr):
        answer += int(v)

    return answer

array = list(range(1, 10001))
for i in range(1, 10001):
    if d(i) in array:
        array.remove(d(i))
for arr in array:
    print(arr)