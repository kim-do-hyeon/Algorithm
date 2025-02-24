# 백준 2015 - 수들의 합 4
# 분류 : 누적합

N, K = map(int, input().split())

arr = list(map(int, input().split()))

sums = [0] * (N + 1)

for i in range(1, N + 1) :
    sums[i] = sums[i - 1] + arr[i - 1]

answer = 0
dic = {}

for i in range(N + 1) :
    if sums[i] - K in dic :
        answer += dic[sums[i] - K]
    dic[sums[i]] = dic.get(sums[i], 0) + 1

print(answer)