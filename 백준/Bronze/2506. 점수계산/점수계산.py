# 백준 2506 - 점수계산
# 분류 : 구현

N = int(input())
scores = list(map(int, input().split()))

answer = 0
score = 0
for i in scores :
    if i == 1 :
        score += 1
        answer += score
    else :
        score = 0
    
print(answer)