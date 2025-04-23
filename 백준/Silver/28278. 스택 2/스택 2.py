# 백준 28278 - 스택 2
# 분류 : 자료구조
import sys
input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N) :
    num = list(map(int, input().split()))
    if len(num) == 1 :
        if num[0] == 2 :
            if len(stack) > 0 :
                print(stack.pop())
            else :
                print(-1)
        elif num[0] == 3 :
            print(len(stack))
        elif num[0] == 4 :
            if len(stack) == 0 :
                print(1)
            else :
                print(0)
        elif num[0] == 5 :
            if len(stack) > 0 :
                print(stack[-1])
            else :
                print(-1)
    elif len(num) == 2 :
        if num[0] == 1 :
            stack.append(num[1])