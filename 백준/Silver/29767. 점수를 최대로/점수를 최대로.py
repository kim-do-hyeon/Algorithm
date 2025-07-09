# 백준 29767 - 점수를 최대로
# 분류 : 누적합 + 그리디

N, K = map(int, input().split())
A = list(map(int, input().split()))

psum = [0] * N
psum[0] = A[0]

for i in range(1, N) :
    psum[i] = psum[i - 1] + A[i]

psum.sort(reverse=True)
print(sum(psum[:K]))