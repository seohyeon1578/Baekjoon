# 1차 효율성 테스트 시간초과 실패패
# def solution(s):
#     answer = True
#     if s.count("(") != s.count(")") or s[0] != "(" or s[-1] != ")":
#         return False
#     stack = []
#     for i in range(len(s)):
#         if s[i] == ")" and stack.count("(") == stack.count(")"):
#             return False
#         stack.append(s[i])
#     return True

# 2차
from collections import deque
def solution(s):
  queue = deque(s)
  cnt_open = 0
  cnt_close = 0   

  while queue:
    q = queue.popleft()

    if q == "(":
      cnt_open += 1
    elif q == ")":
      cnt_close += 1
    if cnt_open < cnt_close:
      return False
    if q == s[0] and q == ")":
      return False
    if q == s[-1] and q== "(":
      return False
  if cnt_open != cnt_close:
    return False
  return True