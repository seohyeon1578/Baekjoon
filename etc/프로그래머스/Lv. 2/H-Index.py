# 1차
def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations) + 1):
        cnt = 0
        for j in citations:
            if j >= i:
                cnt += 1
        if cnt >= i:
            answer = i
            
    return answer
# 2차
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    return max(map(min, enumerate(citations, start=1)))