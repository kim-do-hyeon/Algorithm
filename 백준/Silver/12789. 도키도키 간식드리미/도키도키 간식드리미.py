# 백준 12789 - 도키도키 간식드리미
# 분류 : 자료구조

N = int(input())
line = list(map(int, input().split()))
stack = []
target = 1

for i in line :
    while stack and stack[-1] == target :
        stack.pop()
        target += 1
    if i == target :
        target += 1
    else :
        stack.append(i)

while stack and stack[-1] == target :
    stack.pop()
    target += 1

if not stack :
    print("Nice")
else :
    print("Sad")