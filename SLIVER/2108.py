import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]

arr.sort()
print(round(sum(arr) / N))
print(arr[len(arr) // 2])
dic = dict()
for i in arr:
    if i in dic:
      dic[i] += 1
    else:
      dic[i] = 1
mx = max(dic.values())
mx_arr = []
for i in dic:
   if mx == dic[i]:
    mx_arr.append(i)

if len(mx_arr) > 1:
   print(mx_arr[1])
else:
   print(mx_arr[0])

print(max(arr) - min(arr))