# 백준 9575 - 행운의 수
# 분류 : 브루트포스

T = int(input())
for _ in range(T) :
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    K = int(input())
    C = list(map(int, input().split()))

    lucky = []
    for a in A :
        for b in B :
            for c in C :
                sum = a + b + c
                good = True
                while sum > 0 :
                    if sum % 10 not in [5, 8] :
                        good = False
                        break
                    sum //= 10
                
                if good :
                    lucky.append(a + b + c)

    lucky = list(set(lucky))
    print(len(lucky))