# 백준 9387 - Gholam's Simple Game
t = int(input())
out_lines = []

for _ in range(t):
    M, N = map(int, input().split())

    start_pos = -1
    dir_right = True
    a = list(map(int, input().split()))
    if 2 in a :
        start_pos = a.index(2)
        dir_right = True
    elif 3 in a :
        start_pos = a.index(3)
        dir_right = False

    is_yellow = []
    for i in range(M):
        if a[i] == 0:
            is_yellow.append(True)
        else:
            is_yellow.append(False)

    pos = start_pos
    steps = 0
    yellow_count = 0

    d = 1 if dir_right else -1

    while steps < N:
        if (pos == 0 and d == -1) or (pos == M - 1 and d == 1):
            d = -d
            continue

        pos = pos + d
        steps += 1

        if is_yellow[pos]:
            yellow_count += 1

    print(yellow_count)