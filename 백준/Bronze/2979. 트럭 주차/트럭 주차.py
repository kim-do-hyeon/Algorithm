a, b, c = map(int, input().split())

timeList = [0]*101
answer = 0

for _ in range(3):
    s, e = map(int, input().split())
    for i in range(s, e):
        timeList[i] += 1

for i in timeList:
    if i == 1:
        answer += a
    elif i == 2:
        answer += 2*b
    elif i == 3:
        answer += 3*c

print(answer)