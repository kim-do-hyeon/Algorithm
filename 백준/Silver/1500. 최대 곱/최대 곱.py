# 백준 1500 - 최대 곱
# 분류 : 수학

S, K = map(int, input().split())

q, r = divmod(S, K)

nums = [q + 1] * r + [q] * (K - r)

result = 1
for num in nums :
    result *= num

print(result)