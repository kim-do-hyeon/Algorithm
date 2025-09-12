# [브론즈 2] 백준 1673 - 치킨 쿠폰

while True :
    try :
        N, K = map(int, input().split())
        result = 0
        result += N
        while N // K :
            result += N // K
            N = N // K + N % K
        print(result)
    except :
        break