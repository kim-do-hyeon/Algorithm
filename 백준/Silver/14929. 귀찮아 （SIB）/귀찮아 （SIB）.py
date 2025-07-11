# 백준 14929 - 귀찮아 (SIB)
# 분류 : 수학

N = int(input())
X = list(map(int, input().split()))

sqsum = sum(list(map(lambda x : x ** 2, X)))
print((sum(X) ** 2 - sqsum) // 2)