def solution(users, emoticons):
    answer = [0, 0]
    data = [i for i in range(10, 41, 10) if i >= min(users)[0]]
    discount = []
    
    def dfs(temp, depth):
        if depth == len(temp):
            discount.append(temp[:])
            return
        for d in data:
            temp[depth] += d
            dfs(temp, depth + 1)
            temp[depth] -= d
    
    dfs([0] * len(emoticons), 0)

    for i, dis in enumerate(discount):
        join, price = 0, [0] * len(users)
        for j, emo in enumerate(emoticons):
            for k, user in enumerate(users):
                if user[0] <= dis[j]:
                    price[k] += emo * (100 - dis[j]) // 100
        for k, user in enumerate(users):
            if price[k] >= user[1]:
                join += 1
                price[k]= 0
        if join >= answer[0]:
            if join == answer[0]:
                answer[1] = max(answer[1], sum(price))
            else:
                answer[1] = sum(price)
            answer[0] = join
    return answer

print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],[1300, 1500, 1600, 4900]))