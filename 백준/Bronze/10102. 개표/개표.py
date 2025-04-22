# 백준 10102 - 개표
# 문제집 : Python 배우기 (1 ~ 50)

V = int(input())
S = input()
A = S.count("A")
B = S.count("B")
if A > B :
    print("A")
elif B > A :
    print("B")
elif A == B :
    print("Tie")