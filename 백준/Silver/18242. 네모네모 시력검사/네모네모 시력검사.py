# 백준 18242 - 네모네모 시력검사
# 분류 : 구현

N, M = map(int, input().split())
B = [input() for _ in range(N)]

min_y, max_y, min_x, max_x = 1e9, 0, 1e9, 0

for i in range(N) :
    for j in range(M) :
        if B[i][j] == '#' :
            min_y = min(min_y, i)
            max_y = max(max_y, i)
            min_x = min(min_x, j)
            max_x = max(max_x, j)

center_y, center_x = (min_y + max_y) // 2, (min_x + max_x) // 2

if B[min_y][center_x] == '.' :
    print("UP")
elif B[max_y][center_x] == '.' :
    print("DOWN")
elif B[center_y][min_x] == '.' :
    print("LEFT")
else :
    print("RIGHT")
