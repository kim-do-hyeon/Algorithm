# 백준 7567 - 그릇
# 문제집 : Python 배우기 (1 ~ 50)

height = []
answer = 0
S = input()
for i in S :
    if len(height) == 0 :
        answer += 10
        height.append(i)
    elif height[-1] == "(" and i == "(" :
        answer += 5
        height.append(i)
    elif height[-1] == ")" and i == ")" :
        answer += 5
        height.append(i)
    elif height[-1] == "(" and i == ")" :
        answer += 10
        height.append(i)
    elif height[-1] == ")" and i == "(" :
        answer += 10
        height.append(i)
print(answer)