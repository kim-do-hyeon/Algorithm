# 백준 17213 - 과일 서리
# 분류 : 다이나믹 프로그래밍

N = int(input())
M = int(input())

# M - 1 C M - N
answer = 1
for i in range(1, M - N + 1) :
    answer *= (M - i)
    answer //= i

print(answer)