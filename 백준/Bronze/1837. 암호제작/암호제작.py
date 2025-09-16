# [브론즈 3] 백준 1837 - 암호제작

P, K = map(int, input().split())
bad = True
for i in range(2, K) :
    if P % i == 0 :
        print("BAD", i)
        bad = False
        break
if bad :
    print("GOOD")