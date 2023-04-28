def solution(s):
    answer = [0, 0]
    while len(s) != 1:
        answer[1] += s.count("0")
        s = s.replace("0", "")
        l = len(s)
        s = format(l, "b")
        answer[0] += 1
    return answer