# 1. 내림차순으로 정렬
# 2. s가 가장 큰 수의 s e를 담아둠
# 3. 반복문을 돌려 현재 위치의 e가 가장 큰 수의 s보다 작거나 같다면 answer을 +1 해주고 s가 현재 위치의 s 가 된다
# e가 s보다 크다면 사이에 포함된다는 뜻이기에 e가 s보다 작다면 하나 더 요격을 해야한다.
targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
targets.sort(reverse=True)
s, e = targets[0]
answer = 1
for target in targets:
    s_t, e_t = target
    if e_t <= s:
        answer += 1
        s = s_t
print(answer)