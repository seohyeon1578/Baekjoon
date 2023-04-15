a, b = 0, 1
for i in range(int(input())):
  a, b = b%1000000007, a+b%1000000007
print(a)