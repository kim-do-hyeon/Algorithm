# 백준 1247 - 부호
import sys
input = sys.stdin.readline
for _ in range(3) :
    N = int(input())
    result = 0
    for __ in range(N) :
        result += int(input())
    
    if result == 0 :
        print(0)
    elif result < 0 :
        print("-")
    else :
        print("+")