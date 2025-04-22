# 백준 10886 - 0 = not cute / 1 = cute
# 문제집 : Python 배우기 (1 ~ 50)

N = int(input())
A = {'0' : 0, '1' : 1}
for i in range(N) :
    isCute = input()
    if isCute == '0' :
        A['0'] += 1
    else :
        A['1'] += 1

if A['1'] > A['0'] :
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")