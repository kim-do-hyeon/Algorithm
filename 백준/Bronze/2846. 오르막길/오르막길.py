n = int(input())
pi = list(map(int, input().split()))
a = 0
re = []

for i in range(n-1):
    if pi[i] < pi[i+1]:
        a += pi[i+1] - pi[i]
    else:
        re.append(a)
        a = 0
        
re.append(a)
print(max(re))