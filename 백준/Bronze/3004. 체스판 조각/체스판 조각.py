N = int(input())
answer = 1
a = 1
for i in range(N):
    answer += a
    if i % 2 == 0:
        a += 1
print(answer)