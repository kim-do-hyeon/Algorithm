# 백준 10431 - 줄세우기

P = int(input())
for _ in range(P):
    data = list(map(int, input().split()))
    T = data[0]
    tall = data[1:]

    line = []
    moves = 0

    for s in tall:
        inserted = False
        for i in range(len(line)):
            if line[i] > s:
                moves += len(line) - i
                line.insert(i, s)
                inserted = True
                break
        if not inserted:
            line.append(s)

    print(T, moves)