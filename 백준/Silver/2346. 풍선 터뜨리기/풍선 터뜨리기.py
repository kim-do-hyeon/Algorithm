# 백준 2346 - 풍선 터뜨리기
# 분류 : 자료구조

from collections import deque
N = int(input())
A = list(map(int, input().split()))
Q = deque((i + 1, A[i]) for i in range(N))

answer = []

while Q :
    index, move = Q.popleft()
    answer.append(index)

    if not Q :
        break

    if move > 0 :
        Q.rotate(-(move - 1))
    else :
        Q.rotate(-move)

print(' '.join(map(str, answer)))