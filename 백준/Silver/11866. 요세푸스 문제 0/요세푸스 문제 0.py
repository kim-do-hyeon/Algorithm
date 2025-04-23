# 백준 11866 - 요세푸스 문제 0
# 분류 : 자료구조

N, K = map(int, input().split())

A = []
for i in range(1, N + 1) :
    A.append(i)

answer = []
num = 0

for target in range(N) :
    num += K - 1
    if num >= len(A) :
        num = num % len(A)
    answer.append(str(A.pop(num)))

print("<", ", ".join(answer), ">", sep='')