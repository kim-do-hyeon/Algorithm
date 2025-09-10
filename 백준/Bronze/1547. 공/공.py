# 백준 1547 - 공

ball = [1, 0, 0]
def swap(a, b) :
    global ball
    temp = ball[a - 1]
    ball[a - 1] = ball[b - 1]
    ball[b - 1] = temp
    
M = int(input())
adj = [list(map(int, input().split())) for _ in range(M)]
for i in adj :
    swap(i[0], i[1])

print(ball.index(1) + 1)