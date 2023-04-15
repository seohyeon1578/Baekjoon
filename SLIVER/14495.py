n = int(input())
fibo = [1, 1, 1]
for i in range(3, n):
  fibo.append(fibo[i-3] + fibo[i-1])
print(fibo[-1])
