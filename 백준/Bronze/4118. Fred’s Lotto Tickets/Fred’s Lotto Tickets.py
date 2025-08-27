# 백준 4118 - Fred's Lotto Tickets
import sys
input = sys.stdin.readline
while True :
    N = int(input())
    if N == 0 :
        break
    lottery = [0] * 49
    for _ in range(N) :
        A = list(map(int, input().split()))
        for i in A :
            if lottery[i - 1] == 0 :
                lottery[i - 1] = 1
    if sum(lottery) == 49 :
        print("Yes")
    else :
        print("No")