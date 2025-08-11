T = int(input())
for _ in range(T):
    S1, S2 = input().split()
    dist = []
    for i in range(len(S1)):
        d = (ord(S2[i]) - ord(S1[i]) + 26) % 26
        dist.append(str(d))
    print(f"Distances: {' '.join(dist)}")