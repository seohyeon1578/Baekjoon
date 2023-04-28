def solution(s):
    answer = ""
    array = list(s.split())
    for i in range(len(array)):
      answer += array[i][0].upper() + array[i][1:].lower()
      cur = len(answer)
      
      while cur != len(s) and s[cur] == " ":
         answer += " "
         cur += 1
    return answer
print(solution("3people unFollowed me"))