import sys
input = sys.stdin.readline

def func(x, b):
    if x !=0 and x % b == 0: return 1+func(x//b,b)
    else: return 0

c = [0] * 1001
for x in range(2, 1001):
    c[x] = sum(func(x, b) for b in range(2, x+1))

for _ in range(int(input())):
    x = int(input())
    print(c[x])