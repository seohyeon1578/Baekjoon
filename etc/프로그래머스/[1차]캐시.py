from collections import deque
def solution(cacheSize, cities):
    answer = 0
    stack = deque([])

    if cacheSize == 0:
            answer = len(cities) * 5
    else:
        for city in cities:
            city = city.lower()
            if city not in stack:
                if len(stack) == cacheSize:
                    stack.popleft()
                stack.append(city)
                answer += 5
            else:
                stack.remove(city)
                stack.append(city)
                answer += 1

    return answer
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))