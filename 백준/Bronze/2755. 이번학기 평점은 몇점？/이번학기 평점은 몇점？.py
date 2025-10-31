d = {"A+": 4.3, "A0": 4.0, "A-": 3.7, "B+": 3.3, "B0": 3.0, 
     "B-": 2.7, "C+": 2.3, "C0": 2.0, "C-": 1.7, "D+": 1.3, 
     "D0": 1.0, "D-": 0.7, "F": 0.0}
N = t = 0
for _ in range(int(input())):
    s, n, g = input().split()
    n = int(n) 
    N += n
    t += n*d[g]
print("%.2f" % (round(t/N + 10**-10, 2)))