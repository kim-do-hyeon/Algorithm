# 백준 2010 - 플러그
import sys
input = sys.stdin.readline
answer = 0
N = int(input())
for i in range(N) :
    num = int(input())
    if i == 0 :
        answer += num
    else :
        answer += num - 1
print(answer)