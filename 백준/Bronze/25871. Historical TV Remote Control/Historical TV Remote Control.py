# 백준 25871 -  Historical TV Remote Control
# 분류 : 브루트포스

input_line = input().split()
N = int(input_line[0])
broken = set(map(int, input_line[1:]))
target = int(input())

def valid(channel, broken) :
    for ch in channel :
        if int(ch) in broken :
            return False
    return True

def min_process(target, broken) :
    min_presses = float('inf')

    for ch in range(1000) :
        if valid(str(ch), broken) :
            presses = abs(ch - target)
            min_presses = min(min_presses, presses)
    
    return min_presses

print(min_process(target, broken))