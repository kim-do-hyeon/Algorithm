# 백준 25305 - 커트라인
# 분류 : 정렬

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse = True)
print(A[K - 1])