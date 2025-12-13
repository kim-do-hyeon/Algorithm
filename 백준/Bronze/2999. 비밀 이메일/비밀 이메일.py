str = input()
len = len(str)

x, y = 0, 0

for r in range(1, int(len/2)+1):
    for c in range(r, len+1):
        if r * c == len:
            x, y = r, c

for i in range(x):
    for j in range(y):
        print(str[i + j * x], end='')