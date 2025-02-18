# 백준 2217 - 로프
# 분류 : 그리디

import sys
input = sys.stdin.readline

N = int(input())
W = [0] * N

for i in range(N) :
    W[i] = int(input())

W.sort(reverse = True)

max_weight = True
for i in range(N) :
    # (i + 1)개의 로프를 사용하는 경우에 들 수 있는 최대 무게를 구해줌
    if max_weight < W[i] * (i + 1) :
        max_weight = W[i] * (i + 1)

print(max_weight)