def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer += " "
        elif i.isupper():
            answer += chr((ord(i) - ord("A") + n) % 26 + ord("A"))
        elif i.islower():
            answer += chr((ord(i) - ord("a") + n) % 26 + ord("a"))
    return answer
print(solution("AB", 1))