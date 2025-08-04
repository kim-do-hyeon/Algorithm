# 백준 2455 - 지능형 기차

max_people = 0
current_people = 0
for _ in range(4) :
    OUT, IN = map(int, input().split())
    current_people = current_people - OUT
    current_people += IN
    max_people = max(max_people, current_people)
print(max_people)