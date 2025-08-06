# 백준 1292 - 쉽게 푸는 문제

A, B = map(int, input().split())
X = []
for i in range(1, 1000) :
    for j in range(i) :
        X.append(i)
print(sum(X[A - 1:B]))