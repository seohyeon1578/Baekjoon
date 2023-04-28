def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    
    for i, v in enumerate(answers):
        if one[i % 5] == v:
            score[0] += 1
        if two[i % 8] == v:
            score[1] += 1
        if three[i % 10] == v:
            score[2] +=1
    
    for i, v in enumerate(score):
        if max(score) == v:
            answer.append(i + 1)
            
    return answer