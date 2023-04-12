# 스택 활용
# 처음에는 문자열 find함수를 사용하여 풀려고 하였는데 시간초과가 발생하였다. find를 이용하여 문자열에서 폭발문자열을 계속 없애는 식으로 한다면 새로운 문자열이 계속 생성되기 때문에 시간초과가 발생하는 것 같다.
# 1. 문자열만큼 반복문을 돌려서 문자열을 stack에 하나씩 쌓는다.
# 2. 만약 stack의 뒤에서 부터 폭발문자열의 길이만큼 슬라이싱해서 보았을때 폭발 문자열과 같다면 폭발문자열의 길이만큼 stack에서 빼준다.
# 3. 스택이 비어있지 않다면 리스트를 합쳐서 문자열을 보여주고, 비어있다면 FRULA를 출력한다.

import sys
string = sys.stdin.readline().strip()
boom = [*sys.stdin.readline().strip()]
stack = []

for i in string:
  stack += i
  if stack[-len(boom)::] == boom:
    for _ in range(len(boom)):
      stack.pop()
if stack: 
  print(''.join(stack))
else:
  print('FRULA')