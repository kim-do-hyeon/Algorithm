# 백준 1057 - 토너먼트
# 분류 : 브루트포스

import sys
input = sys.stdin.readline

N, a, b = map(int, input().split())

round = 1

while True :
    if a % 2 == 0 :
        a = a // 2
    else :
        a = a // 2 + 1
    if b % 2 == 0 :
        b = b // 2
    else :
        b = b // 2 + 1
    if a == b :
        print(round)
        break
    round += 1