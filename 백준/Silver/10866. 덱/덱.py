# 백준 10866 - 덱
# 분류 : 덱

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
Deque = deque()
for _ in range(N) :
    data = input().split()
    if len(data) == 2 :
        operator = data[0]
        num = data[1]
        if operator == "push_front" :
            Deque.appendleft(num)
        elif operator == "push_back" :
            Deque.append(num)
    else :
        operator = data[0]
        if operator == "pop_front" :
            if len(Deque) != 0 :
                print(Deque.popleft())
            else :
                print(-1)
        elif operator == "pop_back" :
            if len(Deque) != 0 :
                print(Deque.pop())
            else :
                print(-1)
        elif operator == "size" :
            print(len(Deque))
        elif operator == "empty" :
            if len(Deque) != 0 :
                print(0)
            else :
                print(1)
        elif operator == "front" :
            if len(Deque) != 0 :
                print(Deque[0])
            else :
                print(-1)
        elif operator == "back" :
            if len(Deque) != 0 :
                print(Deque[-1])
            else :
                print(-1)

