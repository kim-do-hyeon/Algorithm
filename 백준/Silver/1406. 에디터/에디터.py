# 백준 1406 - 에디터

import sys
input = sys.stdin.readline

left_stack = list(input().strip())
right_stack = []

for _ in range(int(input())) :
    cmd = input().split()
    if cmd[0] == 'L' and left_stack :
        right_stack.append(left_stack.pop())
    elif cmd[0] == 'D' and right_stack :
        left_stack.append(right_stack.pop())
    elif cmd[0] == 'B' and left_stack :
        left_stack.pop()
    elif cmd[0] == 'P' :
        left_stack.append(cmd[1])

print(''.join(left_stack + right_stack[::-1]))