# 백준 1551 - 수열의 변화

N, K = map(int, input().split())
A = list(map(int, input().split(",")))

for _ in range(K) :
    for i in range(len(A) - 1) :
        A[i] = A[i + 1] - A[i]
    A.pop()
result = ""
for i in A :
    result += str(i) + ","
print(result[:-1])