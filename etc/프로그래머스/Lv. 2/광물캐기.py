# 다이아로 1, 2, 3, 4, 5 깨고, 철로 6, 7, 8을 깨면, 1 + 1 + 1 + 1 + 1 + 5 + 1 + 1 = 12
picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
answer = 0
i = 0
counted = []
flag = True

if sum(picks) * 5 < len(minerals):
    minerals = minerals[:sum(picks) * 5]

while flag:
    target = []
    if i + 5 < len(minerals):
        target = minerals[i: i + 5]
    else:
        target = minerals[i:]
        flag = False
    dias, irons, stones = target.count("diamond"), target.count("iron"), target.count("stone")
    counted.append([dias, irons, stones])
    i += 5
counted.sort(key=lambda x: (-x[0], -x[1]))

for count in counted:
    if picks[0] > 0:
        picks[0] -= 1
        answer += sum(count)
    elif picks[1] > 0:
        picks[1] -= 1
        answer += count[0] * 5 + count[1] + count[2]
    elif picks[2] > 0:
        picks[2] -= 1
        answer += count[0] * 25 + count[1] * 5 + count[2]
    else:
        break
print(answer)