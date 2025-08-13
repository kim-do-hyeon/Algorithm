# 백준 11723 - 집합

import sys
input = lambda: sys.stdin.readline().rstrip()

S = []
M = int(input())
for _ in range(M) :
    line = input().split()
    if len(line) > 1 :
        op = line[0]
        num = int(line[1])

        if op == "add" :
            if num not in S :
                S.append(num)
        elif op == "remove" :
            if num in S :
                S.remove(num)
        elif op == "check" :
            if num in S :
                print("1")
            else :
                print("0")
        elif op == "toggle" :
            if num in S :
                S.remove(num)
            else :
                S.append(num)
    else :
        op = line[0]
        if op == "all" :
            S = [n for n in range(1, 21)]
        elif op == "empty" :
            S = []