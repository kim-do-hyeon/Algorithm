import sys
R, C = map(int, sys.stdin.readline().split())
b = []
for r in range(R):
    a = sys.stdin.readline().strip()
    b += [a + a[::-1]]
b += b[::-1]
 
A, B = map(int, sys.stdin.readline().split())
if b[A-1][B-1] == '#':
    b[A-1] = b[A-1][:B-1] + '.' + b[A-1][B:]
else:
    b[A-1] = b[A-1][:B-1] + '#' + b[A-1][B:]
for r in range(2*R):
    print(b[r])