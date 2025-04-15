# 백준 17298 - 오큰수
# 분류 : 스택

N = int(input())
A = list(map(int, input().split()))

answer = [-1] * N
stack = []

for i in range(N - 1, -1, -1) :
    while len(stack) > 0 and stack[-1] <= A[i] :
        stack.pop(-1)
    
    stack.append(A[i])

    if len(stack) > 1 :
        answer[i] = stack[-2]

print(*answer)