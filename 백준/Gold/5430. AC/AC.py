# 백준 5430 - AC
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    p = list(input())
    n = int(input())
    x = input().replace("[","").replace("]","")
    try :
        x = deque(list(map(int, x.split(","))))
    except :
        x = deque()

    reverse_check = False
    error = False
    for i in p :
        if i == "R" :
            reverse_check = not reverse_check
        elif i == "D" :
            if len(x) >= 1 :
                if reverse_check :
                    x.pop()
                else :
                    x.popleft()
            else :
                print("error")
                error = True
                break
    if not error :
        if reverse_check :
            x.reverse()
        print("[" + ",".join(map(str, x)) + "]")

