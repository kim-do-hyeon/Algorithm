# 백준 28279 - 덱 2
# 분류 : 자료구조

import sys
from collections import deque
input = sys.stdin.readline

Q = deque()
N = int(input())

for i in range(N) :
    A = list(map(int, input().split()))
    if len(A) == 2 :
        if A[0] == 1 :
            Q.appendleft(A[1])
        elif A[0] == 2 :
            Q.append(A[1])
    elif len(A) == 1 :
        if A[0] == 3 :
            if len(Q) > 0 :
                print(Q.popleft())
            else :
                print(-1)
        elif A[0] == 4 :
            if len(Q) > 0 :
                print(Q.pop())
            else :
                print(-1)
        elif A[0] == 5 :
            print(len(Q))
        elif A[0] == 6 :
            if len(Q) > 0 :
                print(0)
            else :
                print(1)
        elif A[0] == 7 :
            if len(Q) > 0 :
                print(Q[0])
            else :
                print(-1)
        elif A[0] == 8 :
            if len(Q) > 0 :
                print(Q[-1])
            else :
                print(-1)