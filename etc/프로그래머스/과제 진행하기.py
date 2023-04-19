from collections import deque

plans =[["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
answer = []
plans.sort(key=lambda x: x[1])
for i in range(len(plans)):
    hh, mm = plans[i][1].split(':')
    plans[i][1] = int(hh) * 60 + int(mm)
    plans[i][2] = int(plans[i][2])  
stack = deque([])
for i in range(len(plans)):
    if i == len(plans) - 1:
        stack.append(plans[i])
        break
    
    name, start, playtime = plans[i]
    next_name, next_start, next_playtime = plans[i + 1]
    
    if start + playtime <= next_start:
       answer.append(name)
       temp_time = next_start - (start + playtime)
       while stack:
           name, start, playtime = stack.pop()
           if temp_time >= playtime:
            answer.append(name)
            temp_time -= playtime
           else:
            temp = [name ,start, playtime - temp_time]
            stack.append(temp)
            break

    else:
        temp = [name, start, (start + playtime) - next_start]
        stack.append(temp)    
while stack:
    name, start, playtime = stack.pop()
    answer.append(name)
print(answer)