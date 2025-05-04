# 백준 17427 - 약수의 합 2
# 분류 : 코딩 테스트 준비 - 기초 ) 수학

N = int(input())
answer = 0
for i in range(1, N + 1) :
    answer += i * (N // i)
print(answer)