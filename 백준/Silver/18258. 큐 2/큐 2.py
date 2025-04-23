# 백준 18258 - 큐 2
# 분류 : 자료구조
# import sys
# input = sys.stdin.readline
# N = int(input())

# queue = []

# for i in range(N) :
#     S = input().split()
#     if len(S) == 2 :
#         operator = S[0]
#         num = int(S[1])
#         if operator == "push" :
#             queue.append(num)
#     elif len(S) == 1 :
#         if S[0] == "pop" :
#             if len(queue) > 0 :
#                 print(queue[0])
#                 queue = queue[1:]
#             else :
#                 print(-1)
#         elif S[0] == "size" :
#             print(len(queue))
#         elif S[0] == "empty" :
#             if len(queue) > 0 :
#                 print(0)
#             else :
#                 print(1)
#         elif S[0] == "front" : 
#             if len(queue) > 0 :
#                 print(queue[0])
#             else :
#                 print(-1)
#         elif S[0] == "back" :
#             if len(queue) > 0 :
#                 print(queue[-1])
#             else :
#                 print(-1)

import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

queue = deque()

for i in range(N) :
    S = input().split()
    if len(S) == 2 :
        operator = S[0]
        num = int(S[1])
        if operator == "push" :
            queue.append(num)
    elif len(S) == 1 :
        if S[0] == "pop" :
            if len(queue) > 0 :
                print(queue.popleft())
            else :
                print(-1)
        elif S[0] == "size" :
            print(len(queue))
        elif S[0] == "empty" :
            if len(queue) > 0 :
                print(0)
            else :
                print(1)
        elif S[0] == "front" : 
            if len(queue) > 0 :
                print(queue[0])
            else :
                print(-1)
        elif S[0] == "back" :
            if len(queue) > 0 :
                print(queue[-1])
            else :
                print(-1)