# 백준 25186 - INFP 두람
# 분류 : 수학

N = int(input())
A = list(map(int, input().split()))

total = sum(A)
if total != 1 and max(A) > total / 2 :
    print("Unhappy")
else :
    print("Happy")