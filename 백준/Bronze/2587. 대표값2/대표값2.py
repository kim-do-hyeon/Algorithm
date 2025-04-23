# 백준 2587 - 대표값2
# 분류 : 정렬

A = [int(input()) for i in range(5)]
A.sort()

print(int(sum(A) / len(A)))
print(A[len(A) // 2])