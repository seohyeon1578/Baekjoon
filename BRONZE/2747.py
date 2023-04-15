# 피보나치 수열

# import sys

# n = int(sys.stdin.readline().strip())
# array = [0, 1, 1]
# for i in range(3, n + 1):
#     array.append(array[i - 2] + array[i - 1])
# print(array[n])

## 숏코딩
a, b = 1, 0
for i in range(int(input())):
    a,b = b, a+b
print(b)