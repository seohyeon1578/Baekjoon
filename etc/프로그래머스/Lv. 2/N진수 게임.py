def solution(n, t, m, p):
    answer = ''
    array = []
    cnt = 0

    for i in range(0, t * m):
        array.append(func(i,n))
    s = ''.join(array)
    
    for i in range(p - 1, len(s), m):
        if cnt >= t:
            break
        answer += s[i]
        cnt += 1
    
    return answer

def func(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return func(q, base) + T[r] if q else T[r]
        
print(solution(16, 16, 2, 2))